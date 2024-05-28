# app/api/depends/enterprise_deps.py
from fastapi import Depends, HTTPException, status
from uuid import UUID
from app.models.enterprise_model import Enterprise
from app.services.enterprise_service import EnterpriseService

async def get_enterprise_by_id(enterprise_id: UUID) -> Enterprise:
    enterprise = await EnterpriseService.get_enterprise_by_id(enterprise_id)
    if not enterprise:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Enterprise not found"
        )
    return enterprise
