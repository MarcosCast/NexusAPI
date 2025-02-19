from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from app.core.security_utils import create_access_token

router = APIRouter()


fake_users_db = {
    "johndoe": {
        "username": "maxmystery",
        "password": "secret123",  
        "full_name": "Marcos Castro"
    }
}

class LoginRequest(BaseModel):
    username: str
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

@router.post("/login", response_model=TokenResponse)
async def login(login_request: LoginRequest):
    """
    A ideia é retonar um JWT nesse endpoint.
    """
    user_data = fake_users_db.get(login_request.username)
    if not user_data or user_data["password"] != login_request.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciais inválidas",
            headers={"WWW-Authenticate": "Bearer"},
        )
    token_data = {"sub": login_request.username}
    access_token = create_access_token(token_data)
    return {"access_token": access_token, "token_type": "bearer"}
