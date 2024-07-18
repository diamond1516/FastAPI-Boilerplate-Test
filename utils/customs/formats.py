from app.core import SETTINGS
from utils.customs.fields import FileObject


class FileFieldFormat(str):
    MEDIA_URL = SETTINGS.MEDIA_URL

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, value):
        if isinstance(value, FileObject):
            return f'{SETTINGS.SERVER_HOST}{cls.MEDIA_URL}{str(value)}'
        return value
