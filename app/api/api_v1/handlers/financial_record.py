from fastapi import APIRouter, Depends, HTTPException, status
from uuid import UUID
from app.schemas.financial_record_schema import FinancialRecordCreate, FinancialRecordOut
from app.services.financial_record_service import FinancialRecordService
from app.api.depends.user_deps import get_current_user
from app.api.depends.financial_record_deps import get_financial_records_by_enterprise_id
from app.models.user_model import User

financial_record_router = APIRouter()

@financial_record_router.post('/create', summary="Create financial record", response_model=FinancialRecordOut)
async def create_financial_record(data: FinancialRecordCreate, current_user: User = Depends(get_current_user)):
    record = await FinancialRecordService.create_financial_record(data)
    return record

@financial_record_router.get('/{enterprise_id}', summary="Get financial records by enterprise ID", response_model=list[FinancialRecordOut])
async def get_financial_records_by_enterprise_id_route(enterprise_id: UUID, current_user: User = Depends(get_current_user)):
    records = await get_financial_records_by_enterprise_id(enterprise_id)
    return records
