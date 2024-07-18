from sqlalchemy import String
from starlette.datastructures import UploadFile
from sqlalchemy.types import TypeDecorator

import os
from werkzeug.utils import secure_filename


class StorageManager:
    def save(self, file, upload_folder):
        raise NotImplementedError

    def get_url(self, filename):
        raise NotImplementedError

    def get_path(self, filename):
        raise NotImplementedError


class LocalStorageManager(StorageManager):
    upload_folder = None

    def save(self, file, upload_folder):
        filename = secure_filename(file.filename)
        file_path = os.path.join(upload_folder, filename)
        with open(file_path, 'wb') as f:
            f.write(file.file.read())
        return file_path

    def get_path(self, filename):
        return os.path.join(self.upload_folder, filename)


class FileField(TypeDecorator):
    impl = String

    def __init__(self, storage_manager, upload_folder, *args, **kwargs):
        self.storage_manager = storage_manager()  # Storage manager obyektini yaratamiz
        self.storage_manager.upload_folder = upload_folder
        self.upload_folder = upload_folder
        super().__init__(*args, **kwargs)

    def process_bind_param(self, value, dialect):
        print(value)
        print(self.upload_folder)
        print(self.storage_manager)
        if isinstance(value, UploadFile):
            file_path = self.storage_manager.save(value)
            print(file_path)
            return file_path
        return str(value)

    def process_result_value(self, value, dialect):
        if value:
            return open(value, 'rb')  # Faylni o'qib olish
        return value  # Qiymatni o'zgarmas qaytaradi

    def file_name(self, value):
        return os.path.basename(value) if value else None  # Fayl nomini qaytaradi

    def file_url(self, value):
        return self.storage_manager.get_url(value) if value else None  # Fayl URL sini qaytaradi

    def file_path(self, value):
        return self.storage_manager.get_path(value, self.upload_folder) if value else None  # Fayl manzilini qaytaradi

    def file_extension(self, value):
        return os.path.splitext(value)[1] if value else None  # Fayl kengaytmasini qaytaradi
