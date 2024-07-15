import os
from pydantic import BaseSettings
from app.core import security
from pathlib import Path
from datetime import timedelta


class DbSettings(BaseSettings):
    ECHO: bool = False
    URL: str = security.DB_SECURITY.get_db_url()


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    WEBSOCKET_PREFIX: str = '/ws'
    ACCESS_TOKEN_EXPIRE: timedelta = timedelta(days=1)
    SERVER_NAME: str = "localhost"
    SERVER_HOST: str = security.MAIN_SECURITY.HOST
    PROJECT_NAME: str = "FastAPI Boilerplate"
    ALGORITHM: str = "RS256"
    PUBLIC_KEY_PATH: Path = security.BASE_DIR / 'keys/public_key.pem'
    PRIVATE_KEY_PATH: Path = security.BASE_DIR / 'keys/private_key.pem'
    DEBUG: bool = True

    class Config:
        case_sensitive = True


SETTINGS = Settings()
DB_SETTINGS = DbSettings()
