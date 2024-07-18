import os
import random
import string
from abc import ABC, abstractmethod
from werkzeug.utils import secure_filename
from app.core.config import SETTINGS


class StorageManager(ABC):
    MEDIA_URL: str = SETTINGS.MEDIA_URL

    @abstractmethod
    def save(self, file, upload_folder):
        raise NotImplementedError

    @abstractmethod
    def delete(self, file):
        raise NotImplementedError

    @classmethod
    def _generate_new_filename(cls, filename):
        name, ext = os.path.splitext(filename)
        random_chars = ''.join(random.choices(string.ascii_letters + string.digits, k=7))
        new_filename = f"{name}_{random_chars}{ext}"

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


LOCAL_STORAGE = LocalStorageManager()
