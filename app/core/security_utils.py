import jwt
from datetime import datetime, timedelta
from app.core.nexus_config import settings

def create_access_token(data: dict) -> str:
    """
    O tolken JWT tem que expirar depois de um tempo
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt
