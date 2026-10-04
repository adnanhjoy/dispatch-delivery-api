from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.modules.auth.auth_schema import LoginResponse, LoginRequest
from app.core.api_response import ApiResponse
from app.config.database import get_db
from .auth_service import loginService

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

# login routes 
@router.post(
        "/login", 
    )
def login(
    payload: LoginRequest, 
    db: Session = Depends(get_db)
):
    data = loginService(
        payload.email, 
        payload.password, 
        db
    )
    return ApiResponse[LoginResponse](
        status_code=200,
        message="Login successful",
        data=data
    )