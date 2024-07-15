import os
from dotenv import load_dotenv
from pathlib import Path
from pydantic import BaseSettings

BASE_DIR = Path(__file__).resolve().parent.parent.parent

dotenv_path = os.path.join(BASE_DIR, '.env')
load_dotenv(dotenv_path)


class MainSecurity(BaseSettings):
    HOST = os.environ.get('HOST', "http://localhost")
    EMAIL_HOST = os.environ.get('EMAIL_HOST', "smtp.gmail.com")
    EMAIL_PORT = int(os.environ.get('EMAIL_PORT', 465))
    EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD', "<PASSWORD>")
    EMAIL = os.environ.get('EMAIL', "<EMAIL>")


class DataBaseSecurity(BaseSettings):
    DB_NAME = os.environ.get('DB_NAME')
    DB_USER = os.environ.get('DB_USER')
    DB_PASSWORD = os.environ.get('DB_PASSWORD')
    DB_HOST = os.environ.get('DB_HOST')
    DB_PORT = os.environ.get('DB_PORT')
    DB_ENGINE = os.environ.get('DB_ENGINE')

    def get_db_url(self):
        return f"{self.DB_ENGINE}://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


MAIN_SECURITY = MainSecurity()
DB_SECURITY = DataBaseSecurity()
