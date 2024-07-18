from app.core import SETTINGS


class FileFieldFormat(str):

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, value):
        return f'{SETTINGS.SERVER_HOST}{value}'
