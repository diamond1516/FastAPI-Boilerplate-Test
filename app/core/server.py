from fastapi import FastAPI
from app.api.api import __routes__


class Server:
    __app: FastAPI

    def __init__(self, app: FastAPI):
        self.__app = app
        self.__register_routes(app)
        self.__register_events(app)

    def get_app(self):
        return self.__app

    @staticmethod
    def __register_routes(app):
        __routes__.register_routes(app)

    @staticmethod
    def __register_events(app: FastAPI):
        app.on_event('startup')
