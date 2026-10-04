from datetime import datetime, timedelta, timezone
import jwt

from app.config import settings


def create_access_token(payload: dict) -> str:
    to_encode = payload.copy()

    expire = datetime.now(timezone.utc) + timedelta(
        minutes=30
    )

    to_encode.update({
        "exp": expire,
    })

    return jwt.encode(
        to_encode,
        settings.JWT_SECRET_KEY,
        algorithm="HS256",
    )


def decode_access_token(token: str) -> dict:
    return jwt.decode(
        token,
        settings.JWT_SECRET_KEY,
        algorithms=["HS256"],
    )