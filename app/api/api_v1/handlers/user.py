# app/api/api_v1/handlers/user.py
from fastapi import APIRouter, HTTPException, status
import pymongo
import pymongo.errors
from app.schemas.user_schema import UserAuth, UserOut
from app.services.user_service import UserService

user_router = APIRouter()

@user_router.post('/create', summary="Create new user", response_model=UserOut)
async def create_user(data: UserAuth):
    try:
        user = await UserService.create_user(data)
        return user
    except pymongo.errors.DuplicateKeyError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The user or username already exists"
        )
