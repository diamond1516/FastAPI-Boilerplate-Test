from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.api import __routes__
from app.core import SETTINGS


async def on_startup() -> None:
    print('The app is working 🎊🎉🎛')


class Server:
    __app: FastAPI

    def __init__(self, app: FastAPI):
        self.__app = app
        self.__register_routes(app)
        self.__register_events(app)
        self.__register_middlewares(app)
        self.__register_websocket(app)
        self.__register_media_files(app)

    def get_app(self):
        return self.__app

    @staticmethod
    def __register_routes(app):
        __routes__.register_routes(app)

    @staticmethod
    def __register_websocket(app):
        pass

    @staticmethod
    def __register_events(app: FastAPI):
        app.on_event('startup')(on_startup)

    @staticmethod
    def __register_middlewares(app: FastAPI):
        app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    @classmethod
    def __register_media_files(cls, app: FastAPI):
        app.mount(f'/{SETTINGS.MEDIA_URL}', StaticFiles(directory="media"), name="media")
