import os
from pydantic import BaseSettings
from app.core import security
from pathlib import Path


BASE_DIR = security.BASE_DIR


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    SERVER_NAME: str = "localhost"
    SERVER_HOST: str = os.getenv("SERVER_HOST", "http://localhost")
    PROJECT_NAME: str = "FastAPI Boilerplate"
    SQLALCHEMY_DATABASE_URI: str = security.DATABASE_URI
    ALGORITHM: str = "RS256"
    PUBLIC_KEY_PATH: Path = BASE_DIR / 'keys/public.pem'
    PRIVATE_KEY_PATH: Path = BASE_DIR / 'keys/private.pem'

    class Config:
        case_sensitive = True


settings = Settings()
