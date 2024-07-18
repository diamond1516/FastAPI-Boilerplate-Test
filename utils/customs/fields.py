import os

from sqlalchemy import String
from sqlalchemy.types import TypeDecorator
from starlette.datastructures import UploadFile
from app.core.storages import LOCAL_STORAGE


class FileObject(object):
    def __init__(self, path):
        self.path = path

    def __repr__(self):
        return self.path

    @property
    def filename(self):
        return os.path.basename(self.path)

    @property
    def file_url(self):
        return self.path

    @property
    def extension(self):
        return os.path.splitext(self.path)[1]

    @property
    def file(self):
        return UploadFile(self.path).file

    def __str__(self):
        return str(self.path)


class FileField(TypeDecorator):
    impl = String

    def __init__(self, upload_folder, storage_manager=LOCAL_STORAGE, *args, **kwargs):
        self.storage_manager = storage_manager
        self.upload_folder = upload_folder
        super().__init__(*args, **kwargs)

    def process_bind_param(self, value, dialect):
        if isinstance(value, (UploadFile, FileObject)):
            file_path = self.storage_manager.save(value, self.upload_folder)
            return file_path
        return str(value)

    def process_result_value(self, value, dialect) -> FileObject:
        return FileObject(value)
