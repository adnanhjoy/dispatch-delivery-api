from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.config.database import get_db
from .auth_service import loginService

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

@router.post("/login")
def login(email: str, password: str, db: Session = Depends(get_db)):
    return loginService(email, password, db)