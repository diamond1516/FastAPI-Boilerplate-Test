from app.core import SETTINGS


class FileFieldFormat(str):
    MEDIA_URL = SETTINGS.MEDIA_URL

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, value):
        return f'{SETTINGS.SERVER_HOST}{cls.MEDIA_URL}{str(value)}'
