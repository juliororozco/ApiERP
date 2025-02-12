# app/models/user_model.py
from typing import Optional
from datetime import datetime
from uuid import UUID, uuid4
from beanie import Document, Indexed
from pydantic import Field, EmailStr

class User(Document):
    user_id: UUID = Field(default_factory=uuid4)
    username: str = Indexed(unique=True)
    email: EmailStr = Indexed(unique=True)
    hashed_password: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    disable: Optional[bool] = None

    def __repr__(self) -> str:
        return f"<User {self.email}>"
    
    def __str__(self) -> str:
        return self.email
    
    def __hash__(self) -> int:
        return hash(self.email)
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, User):
            return self.email == other.email
        return False

    @property
    def created(self) -> datetime:
        return self.id.generation_time
    
    @classmethod
    async def by_email(cls, email: str) -> "User":
        return await cls.find_one(cls.email == email)
    
    class Settings:
        collection = "users"

