from fastapi import FastAPI
from app.core import Server, SETTINGS


def app(_=None) -> FastAPI:
    main = FastAPI(
        title=SETTINGS.PROJECT_NAME,
        debug=SETTINGS.DEBUG,
    )
    return Server(main).get_app()
