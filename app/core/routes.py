from fastapi import FastAPI
from dataclasses import dataclass
from app.core.config import SETTINGS


@dataclass(frozen=True)
class Routes:

    routers: tuple

    def register_routes(self, app: FastAPI):

        for router in self.routers:
            app.include_router(router, prefix=SETTINGS.API_V1_STR)
