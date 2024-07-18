from typing import List

from fastapi import APIRouter, Depends, UploadFile, File, Request
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from pydantic import BaseModel

from app.api import deps
from app.models.test import TestModel

router = APIRouter(
    prefix="/test",
    tags=["test"],
)


def get_file_url(file_path: str) -> str:
    from starlette.routing import Router
    _router = Router()
    return _router.url_path_for("media/", path=file_path)


@router.post('/file-upload/')
async def upload_file(
        file: UploadFile = File(...),
        db: AsyncSession = Depends(deps.get_db),
):
    new_obj = TestModel(file=file)
    db.add(new_obj)
    await db.commit()
    await db.refresh(new_obj)

    return new_obj


class FormattedDatetime(str):

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, value):

        print(value.extension)
        print(value)
        return f'http://127.0.0.1:8001/{value}'


class Image(BaseModel):
    file: FormattedDatetime

    class Config:
        orm_mode = True


@router.get(
    "/file",
    response_model=List[Image],
)
async def get_file(
        db: AsyncSession = Depends(deps.get_db),

):
    result = await db.execute(select(TestModel))
    return result.scalars().all()
