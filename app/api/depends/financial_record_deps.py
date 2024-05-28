from fastapi import Depends, HTTPException, status
from uuid import UUID
from app.services.financial_record_service import FinancialRecordService

async def get_financial_records_by_enterprise_id(enterprise_id: UUID):
    records = await FinancialRecordService.get_financial_records_by_enterprise_id(enterprise_id)
    if not records:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Financial records not found"
        )
    return records
