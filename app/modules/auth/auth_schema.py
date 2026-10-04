from pydantic import BaseModel, EmailStr

class LoginResponse(BaseModel):
    access_token: str
    data: dict

class LoginRequest(BaseModel):
    email: EmailStr
    password: str