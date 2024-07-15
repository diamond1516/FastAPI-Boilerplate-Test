import bcrypt


def hash_password(password) -> bytes:
    salt = bcrypt.gensalt()
    pwd_bytes: bytes = password.encode('utf-8')
    return bcrypt.hashpw(pwd_bytes, salt)


def verify_password(password: str, hashed_password: bytes) -> bool:
    return bcrypt.checkpw(
        password.encode('utf-8'),
        hashed_password
    )


