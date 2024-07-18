from typing import List

from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from pydantic import BaseModel

from app.api import deps
from app.models.test import TestModel

router = APIRouter(
    prefix="/test",
    tags=["test"],
)


class FormattedDatetime(str):
    MEDIA_URL = ''

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, value):
        return f'http://127.0.0.1:8000/{cls.MEDIA_URL}{value}'


class Image(BaseModel):
    file: FormattedDatetime

    class Config:
        orm_mode = True


def get_file_url(file_path: str) -> str:
    from starlette.routing import Router
    _router = Router()
    return _router.url_path_for("media/", path=file_path)


@router.post(
    '/file-upload/',
    response_model=Image,
)
async def upload_file(
        file: UploadFile = File(...),
        db: AsyncSession = Depends(deps.get_db),
):
    new_obj = TestModel(file=file)
    db.add(new_obj)
    await db.commit()
    await db.refresh(new_obj)

    return new_obj


@router.get(
    "/file",
    response_model=List[Image],
)
async def get_file(
        db: AsyncSession = Depends(deps.get_db),

):
    result = await db.execute(select(TestModel))
    items = result.scalars().all()

    first_item = items[0]

    new = TestModel(file=first_item.file)

    db.add(new)
    await db.commit()
    await db.refresh(new)

    return items
