from typing import Optional
from uuid import UUID
from app.models.financial_record_model import FinancialRecord
from app.schemas.financial_record_schema import FinancialRecordCreate

class FinancialRecordService:
    @staticmethod
    async def create_financial_record(data: FinancialRecordCreate) -> FinancialRecord:
        financial_record = FinancialRecord(
            enterprise_id=data.enterprise_id,
            type=data.type,
            amount=data.amount,
            description=data.description
        )
        await financial_record.insert()
        return financial_record

    @staticmethod
    async def get_financial_records_by_enterprise_id(enterprise_id: UUID):
        return await FinancialRecord.find(FinancialRecord.enterprise_id == enterprise_id).to_list()

    @staticmethod
    async def update_financial_record_on_employee_change(enterprise_id: UUID, type: str, amount: float, description: str):
        financial_record = FinancialRecord(
            enterprise_id=enterprise_id,
            type=type,
            amount=amount,
            description=description
        )
        await financial_record.insert()
        return financial_record
