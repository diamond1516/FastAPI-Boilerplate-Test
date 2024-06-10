import jwt
from app.core.config import settings


async def encode_jwt(
        payload,
        algorithm=settings.ALGORITHM,
        private_key: str = settings.PRIVATE_KEY_PATH.read_text(),
):
    return jwt.encode(
        payload,
        private_key,
        algorithm=algorithm,
    )


async def decode_jwt(
        token: str,
        public_key: str = settings.PUBLIC_KEY_PATH.read_text(),
        algorithm: str = settings.ALGORITHM,
):
    return jwt.decode(
        token,
        public_key,
        algorithms=[algorithm],
    )
