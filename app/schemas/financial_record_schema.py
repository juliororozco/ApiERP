from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime

class FinancialRecordCreate(BaseModel):
    enterprise_id: UUID
    type: str
    amount: float
    description: Optional[str] = None

class FinancialRecordOut(BaseModel):
    record_id: UUID
    enterprise_id: UUID
    type: str
    amount: float
    date: datetime
    description: Optional[str] = None
