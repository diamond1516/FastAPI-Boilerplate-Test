from app.core.config import settings
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker


class DbHelper:
    def __init__(self, url, echo: bool):
        self.engine = create_async_engine(url, echo=echo)
        self.session_factory = async_sessionmaker(
            self.engine,
            expire_on_commit=False,
            class_=AsyncSession,
            autoflush=False,
            autocommit=False
        )


db_helper = DbHelper(settings.SQLALCHEMY_DATABASE_URI, settings.DB_ECHO)
