# app/schemas/user_schema.py
from uuid import UUID
from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UserAuth(BaseModel):
    email: EmailStr = Field(..., description="User email")
    username: str = Field(..., min_length=5, max_length=50, description="User username")
    password: str = Field(..., min_length=5, max_length=50, description="User password")
    first_name: Optional[str] = Field(None, description="First name")
    last_name: Optional[str] = Field(None, description="Last name")
    disable: Optional[bool] = Field(None, description="Disable user")

class UserOut(BaseModel):
    user_id: UUID
    username: str
    email: EmailStr
    first_name: Optional[str]
    last_name: Optional[str]
    disable: bool = False
