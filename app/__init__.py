from fastapi import FastAPI
from app.core.server import Server


def app(_=None) -> FastAPI:
    main = FastAPI()
    return Server(main).get_app()


