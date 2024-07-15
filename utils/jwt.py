import jwt
from app.core import SETTINGS
from datetime import datetime


async def encode_jwt(
        payload: dict,
        algorithm=SETTINGS.ALGORITHM,
        private_key: str = SETTINGS.PRIVATE_KEY,
):

    payload.update(
        exp=datetime.utcnow() + SETTINGS.ACCESS_TOKEN_EXPIRE,
        iat=datetime.utcnow(),
    )
    return jwt.encode(
        payload,
        private_key,
        algorithm=algorithm,
    )


async def decode_jwt(
        token: str,
        public_key: str = SETTINGS.PUBLIC_KEY,
        algorithm: str = SETTINGS.ALGORITHM,
):
    return jwt.decode(
        token,
        public_key,
        algorithms=[algorithm],
    )
