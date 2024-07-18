from sqlalchemy import Column, String, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship
from app.models.base import BaseModel
from utils.customs.fields import FileField
from app.core.storages import LOCAL_STORAGE


class Product(BaseModel):
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    images = relationship("TestModel", back_populates="product")


class TestModel(BaseModel):
    file = Column(FileField(storage_manager=LOCAL_STORAGE, upload_folder='products/', length=255))
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    product = relationship("Product", back_populates="images")
