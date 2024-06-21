from fastapi import FastAPI
from app.core.server import Server
from app.core.config import SETTINGS


def app(_=None) -> FastAPI:
    main = FastAPI(
        title=SETTINGS.PROJECT_NAME,
        debug=SETTINGS.DEBUG,
    )
    return Server(main).get_app()
