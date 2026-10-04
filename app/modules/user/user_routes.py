from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.config.database import get_db
from app.core.api_response import ApiResponse
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


@router.get("/")
def get_all_users_route(
    db: Session = Depends(get_db),
):
    data = get_all_users(db)
    return ApiResponse[list[UserResponse]](
        status_code=200,
        message="Success",
        data=data
    ) 