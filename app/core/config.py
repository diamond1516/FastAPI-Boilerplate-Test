import os
from pydantic import BaseSettings
from app.core import security


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    SERVER_NAME: str = "localhost"
    SERVER_HOST: str = os.getenv("SERVER_HOST", "http://localhost")
    PROJECT_NAME: str = "FastAPI Boilerplate"
    SQLALCHEMY_DATABASE_URI: str = security.DATABASE_URI

    class Config:
        case_sensitive = True


settings = Settings()
