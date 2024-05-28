from typing import Optional
from uuid import UUID, uuid4
from datetime import datetime
from beanie import Document
from pydantic import Field, EmailStr

class Employee(Document):
    employee_id: UUID = Field(default_factory=uuid4)
    enterprise_id: UUID
    name: str
    email: EmailStr
    phone: str
    position: str
    salary: float
    hire_date: datetime = Field(default_factory=datetime.utcnow)
    termination_date: Optional[datetime] = None
    cedula: str

    class Settings:
        collection = "employees"
