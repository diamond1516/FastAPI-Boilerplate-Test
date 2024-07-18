from sqlalchemy import Column
from app.models.base import BaseModel
from utils.customs.fields import FileField
from app.core.storages import LOCAL_STORAGE


class TestModel(BaseModel):
    file = Column(FileField(storage_manager=LOCAL_STORAGE, upload_folder='salom/', length=255))
