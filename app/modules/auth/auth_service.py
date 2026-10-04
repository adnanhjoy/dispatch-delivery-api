from sqlalchemy.orm import Session
from app.modules.user.user_model import User 
from app.core.api_error import ApiError
import bcrypt

def loginService(email, password, db: Session):
    isExist = db.query(User).filter(User.email == email).first()
    if isExist is None:
        raise ApiError(404, "User not found")
    validPassword = bcrypt.checkpw(password.encode("utf-8"), isExist.password.encode("utf-8"))
    if not validPassword:
        raise ApiError(401, "Invalid password")
    return isExist