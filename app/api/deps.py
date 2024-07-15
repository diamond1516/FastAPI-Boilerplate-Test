from typing import AsyncGenerator

from app.db import db_helper


async def get_db() -> AsyncGenerator:
    return db_helper.get_scoped_session()


