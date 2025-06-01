from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone
from fastapi import HTTPException


SECRET_KEY = "YKHbD1vkstb3MfS8LkQ9jbbWRtTvKTn2G3cP5j3aDo0"
ALGORITHM = "HS256"

def create_token(user_id: int, expires_delta: timedelta = timedelta(hours=1)):
    to_encode = {"sub": str(user_id), "exp": datetime.now(timezone.utc) + expires_delta}
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def decode_token(token: str):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
