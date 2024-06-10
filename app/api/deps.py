from typing import Generator
from app.db.session import async_session


def get_db() -> Generator:
    try:
        db = async_session()
        yield db
    finally:
        db.close()

