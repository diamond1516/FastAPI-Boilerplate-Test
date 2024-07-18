from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.ext.asyncio import AsyncSession

from app.api import deps
from app.models.test import TestModel

router = APIRouter(
    prefix="/test",
    tags=["test"],
)


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

