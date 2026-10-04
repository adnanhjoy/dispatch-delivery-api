from sqlalchemy.orm import Session
import bcrypt

from .user_model import User
from .user_schema import UserSchema


def create_user(user: UserSchema, db: Session):
    if db.query(User).filter(User.email == user.email).first():
        return None
    hashed_password = bcrypt.hashpw(
        user.password.encode("utf-8"),
        bcrypt.gensalt()
    ).decode("utf-8")

    user_data = user.model_dump()
    user_data["password"] = hashed_password

    new_user = User(**user_data)
    print('password',hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def get_all_users(db: Session):

    users = db.query(User).all()

    return users