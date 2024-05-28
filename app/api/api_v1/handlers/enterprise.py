# app/api/api_v1/handlers/enterprise.py
from fastapi import APIRouter, HTTPException, status, Depends
from uuid import UUID
import pymongo
from app.models.enterprise_model import Enterprise
from app.schemas.enterprise_schema import EnterpriseCreate, EnterpriseOut, EnterpriseUpdate
from app.services.enterprise_service import EnterpriseService
from app.api.depends.user_deps import get_current_user
from app.api.depends.enterprise_deps import get_enterprise_by_id
from app.models.user_model import User

enterprise_router = APIRouter()

@enterprise_router.post('/create', summary="Create new enterprise", response_model=EnterpriseOut)
async def create_enterprise(data: EnterpriseCreate, current_user: User = Depends(get_current_user)):
    try:
        enterprise = await EnterpriseService.create_enterprise(data, owner_id=current_user.user_id)
        return enterprise
    except pymongo.errors.DuplicateKeyError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The enterprise name or tax ID already exists"
        )

@enterprise_router.get('/{enterprise_id}', summary="Get enterprise by ID", response_model=EnterpriseOut)
async def get_enterprise_by_id_route(enterprise: Enterprise = Depends(get_enterprise_by_id)):
    return enterprise

@enterprise_router.put('/{enterprise_id}', summary="Update enterprise", response_model=EnterpriseOut)
async def update_enterprise(enterprise_id: UUID, data: EnterpriseUpdate, current_user: User = Depends(get_current_user), enterprise: Enterprise = Depends(get_enterprise_by_id)):
    if enterprise.owner_id != current_user.user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to update this enterprise"
        )
    updated_enterprise = await EnterpriseService.update_enterprise(enterprise_id, data)
    return updated_enterprise
