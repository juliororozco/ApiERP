# app/models/enterprise_model.py
from typing import Optional
from uuid import UUID, uuid4
from datetime import datetime
from beanie import Document
from pydantic import Field, EmailStr

class Enterprise(Document):
    enterprise_id: UUID = Field(default_factory=uuid4)
    name: str
    address: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[EmailStr] = None
    tax_id: Optional[str] = None
    owner_id: UUID
    registration_date: datetime = Field(default_factory=datetime.utcnow)

    class Settings:
        collection = "enterprises"
