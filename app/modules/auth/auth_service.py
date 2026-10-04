from sqlalchemy.orm import Session
from app.modules.user.user_model import User 
from app.core.api_error import ApiError
import bcrypt
from app.utils.token_generate import create_access_token

# login service 
def loginService(email, password, db: Session):
    isExist = db.query(User).filter(User.email == email).first()

    if isExist is None:
        raise ApiError(404, "User not found")

    if isExist.status == "inactive":
        raise ApiError(401, "Your account is inactive")
    
    validPassword = bcrypt.checkpw(password.encode("utf-8"), isExist.password.encode("utf-8"))

    if not validPassword:
        raise ApiError(401, "Invalid password")
    
    payload = {
        "id": isExist.id,
        "name": isExist.name,
        "email": isExist.email,
    }

    token = create_access_token(payload)

    return {
        "access_token": token,
        "data": payload
    }