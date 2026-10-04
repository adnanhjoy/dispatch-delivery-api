from pydantic import BaseModel, EmailStr
from typing import Optional
from enum import Enum

class StatusEnum(str, Enum):
    active = "active"
    inactive = "inactive"

class UserSchema(BaseModel):
    name: str
    email: EmailStr
    password: str
    status: StatusEnum = StatusEnum.inactive
    phone: Optional[str]
    address: Optional[str]



class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

    model_config = {
        "from_attributes": True
    }