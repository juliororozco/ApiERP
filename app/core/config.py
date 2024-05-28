# app/core/config.py
from typing import List
from pydantic_settings import BaseSettings
from pydantic import AnyHttpUrl
from decouple import config

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    JWT_SECRET_KEY: str = config("JWT_SECRET_KEY", cast=str)
    JWT_REFRESH_SECRET_KEY: str = config("JWT_REFRESH_SECRET_KEY", cast=str)
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60*24*7
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    PROJECT_NAME: str = "ERP"
    MONGO_DB_CONNECTION: str = config("MONGO_DB_CONNECTION", cast=str)

    class Config:
        case_sensitive = True

settings = Settings()
