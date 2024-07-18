from sqlalchemy import String
from fastapi.datastructures import UploadFile

import os
from abc import ABC, abstractmethod
from werkzeug.utils import secure_filename


class StorageManager:
    def save(self, file):
        raise NotImplementedError

    def get_url(self, filename):
        raise NotImplementedError

    def get_path(self, filename):
        raise NotImplementedError


class LocalStorageManager(StorageManager):
    upload_folder = None

    def save(self, file):
        filename = secure_filename(file.filename)
        file_path = os.path.join(self.upload_folder, filename)
        with open(file_path, 'wb') as f:
            f.write(file.file.read())
        return file_path

    def get_path(self, filename):
        return os.path.join(self.upload_folder, filename)


class FileField(String):
    def __init__(self, storage_manager, upload_folder, *args, **kwargs):
        self.storage_manager = storage_manager()
        self.storage_manager.upload_folder = upload_folder

        self.upload_folder = upload_folder
        super().__init__(*args, **kwargs)

    def process_bind_param(self, value, dialect):
        if isinstance(value, UploadFile):
            file_path = self.storage_manager.save(value)
            return file_path
        return value

    def process_result_value(self, value, dialect):
        if value:
            return open(value, 'rb')
        return value

    def file_name(self, value):
        return os.path.basename(value)

    def file_url(self, value):
        return self.storage_manager.get_url(value)

    def file_path(self, value):
        return self.storage_manager.get_path(value, self.upload_folder)

    def file_extension(self, value):
        return os.path.splitext(value)[1]
