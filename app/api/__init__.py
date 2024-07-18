from app.core.routes import Routes
from app.api.views.test import router

__routes__ = Routes(routers=(router,))
