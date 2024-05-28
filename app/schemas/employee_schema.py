from pydantic import BaseModel, EmailStr
from typing import Optional
from uuid import UUID
from datetime import datetime

class EmployeeCreate(BaseModel):
    enterprise_id: UUID
    name: str
    email: EmailStr
    phone: str
    position: str
    salary: float
    cedula: str

class EmployeeUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    position: Optional[str] = None
    salary: Optional[float] = None
    termination_date: Optional[datetime] = None
    cedula: Optional[str] = None

class EmployeeOut(BaseModel):
    employee_id: UUID
    enterprise_id: UUID
    name: str
    email: EmailStr
    phone: str
    position: str
    salary: float
    hire_date: datetime
    termination_date: Optional[datetime] = None
    cedula: str
