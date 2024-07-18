from pydantic import BaseSettings
from app.core import security
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
    PUBLIC_KEY: str = (security.BASE_DIR / 'keys/public_key.pem').read_text()
    PRIVATE_KEY: str = (security.BASE_DIR / 'keys/private_key.pem').read_text()
    DEBUG: bool = True
    MEDIA_URL: str = '/media'

    class Config:
        case_sensitive = True


SETTINGS = Settings()
DB_SETTINGS = DbSettings()
