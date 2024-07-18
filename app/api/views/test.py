from typing import List
from fastapi import APIRouter, Depends, UploadFile, File, Form
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel
from app.api import deps
from app.models.test import TestModel, Product
from utils.customs import FileFieldFormat
import json

router = APIRouter(
    prefix="/test",
    tags=["test"],
)


class Image(BaseModel):
    file: FileFieldFormat

    class Config:
        orm_mode = True


class ProductSchema(BaseModel):
    name: str
    price: float
    images: List[Image]

    class Config:
        orm_mode = True


@router.post(
    '/products/',
    response_model=ProductSchema,
)
async def create_product(
        data: str = Form(...),
        images: List[UploadFile] = File(...),
        db: AsyncSession = Depends(deps.get_db),
):
    data = json.loads(data)
    product = Product(**data)
    db.add(product)
    await db.flush()

    for image in images:
        image = TestModel(
            file=image,
            product_id=product.id
        )
        db.add(image)

    await db.commit()
    await db.refresh(product, attribute_names=['images'])

    return ProductSchema(
        name=product.name,
        price=product.price,
        images=product.images,
    )


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
