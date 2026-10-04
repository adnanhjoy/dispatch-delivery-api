from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.config.database import get_db

from .user_schema import UserSchema, UserResponse
from .user_service import create_user, get_all_users


router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.post("/", response_model=UserResponse)
def create_user_route(
    user: UserSchema,
    db: Session = Depends(get_db),
):
    return create_user(user, db)


@router.get("/", response_model=list[UserResponse])
def get_all_users_route(
    db: Session = Depends(get_db),
):
    return get_all_users(db)