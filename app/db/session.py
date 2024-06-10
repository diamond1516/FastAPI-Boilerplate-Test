from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

DATABASE_URL = settings.SQLALCHEMY_DATABASE_URI

engine = create_async_engine(DATABASE_URL, echo=True, pool_size=20, max_overflow=0)

async_session = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)
