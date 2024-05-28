from typing import Optional
from uuid import UUID, uuid4
from datetime import datetime
from beanie import Document
from pydantic import Field

class FinancialRecord(Document):
    record_id: UUID = Field(default_factory=uuid4)
    enterprise_id: UUID
    type: str
    amount: float
    date: datetime = Field(default_factory=datetime.utcnow)
    description: Optional[str] = None

    class Settings:
        collection = "financial_records"
