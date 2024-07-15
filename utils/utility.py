import random
import smtplib
import ssl
import uuid

from app.core import MAIN_SECURITY
from email.message import EmailMessage


class Utility:

    @classmethod
    async def generate_four_digit_number(cls):
        return str(random.randint(1000, 9999))

    @classmethod
    async def get_jwt_payload(cls, user: object) -> dict:
        user_data = user.__dict__
        return dict(
            sub=user_data['id'],
            username=user_data['username'],
        )

    @classmethod
    async def send_msg_email(cls, email, msg):
        subject = "FastAPI AUTH Test"
        em = EmailMessage()
        em['Message-ID'] = str(uuid.uuid4())
        em['From'] = MAIN_SECURITY.EMAIL
        em['To'] = email
        em['Subject'] = subject
        em.set_content(msg)
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(MAIN_SECURITY.EMAIL_HOST, MAIN_SECURITY.EMAIL_PORT, context=context) as smtp:
            smtp.login(MAIN_SECURITY.EMAIL, MAIN_SECURITY.EMAIL_PASSWORD)
            smtp.sendmail(MAIN_SECURITY.EMAIL, email, em.as_string())


UTILITY = Utility()
