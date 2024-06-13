from fastapi import FastAPI
from app.api.api import api_router
from app.core.config import SETTINGS

app = FastAPI(title=SETTINGS.PROJECT_NAME)

app.include_router(api_router, prefix=SETTINGS.API_V1_STR)
