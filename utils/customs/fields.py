import random
from datetime import datetime

from sqlalchemy import String
from starlette.datastructures import UploadFile
from sqlalchemy.types import TypeDecorator
from abc import ABC, abstractmethod

import os
from werkzeug.utils import secure_filename


class FileObject(object):
    def __init__(self, path):
        self.path = path

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


class StorageManager(ABC):
    MEDIA_URL = 'media/'

    @abstractmethod
    def save(self, file, upload_folder):
        raise NotImplementedError

    @abstractmethod
    def delete(self, file):
        raise NotImplementedError

    @classmethod
    def _generate_new_filename(cls, filename):
        name, ext = os.path.splitext(filename)
        extra = str(random.randint(1, 100))
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        new_filename = f"{name}{extra}_{timestamp}{ext}"
        return new_filename


class LocalStorageManager(StorageManager):

    def save(self, file, upload_folder):
        new_filename = self._generate_new_filename(secure_filename(file.filename))
        folder_path = os.path.join(self.MEDIA_URL, upload_folder)
        file_path = os.path.join(folder_path, new_filename)

        os.makedirs(folder_path, exist_ok=True)
        with open(file_path, 'wb') as f:
            f.write(file.file.read())

        return file_path.replace(self.MEDIA_URL, '')

    def delete(self, path):
        file_path = os.path.join(self.MEDIA_URL, path)
        if os.path.exists(file_path):
            os.remove(file_path)


class FileField(TypeDecorator):
    impl = String

    def __init__(self, storage_manager, upload_folder, *args, **kwargs):
        self.storage_manager = storage_manager()
        self.storage_manager.upload_folder = upload_folder
        self.upload_folder = upload_folder
        super().__init__(*args, **kwargs)

    def process_bind_param(self, value, dialect):

        if isinstance(value, (UploadFile, FileObject)):
            file_path = self.storage_manager.save(value, self.upload_folder)
            return file_path
        return str(value)

    def process_result_value(self, value, dialect) -> FileObject:
        return FileObject(value)
