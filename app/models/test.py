from sqlalchemy import Column, Integer, String
from app.models.base import BaseModel
from utils.customs.fields import FileField


class TestModel(BaseModel):
    file = Column(FileField(storage_manager=LocalStorageManager, upload_folder='salom/', length=255))
