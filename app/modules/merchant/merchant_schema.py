from datetime import datetime
from pydantic import BaseModel, ConfigDict
from app.modules.user.user_schema import UserResponse


class MerchantBase(BaseModel):
    business_name: str | None = None
    business_phone: str | None = None
    business_address: str | None = None
    trade_license: str | None = None


class MerchantCreate(MerchantBase):
    user_id: int


class MerchantUpdate(BaseModel):
    business_name: str | None = None
    business_phone: str | None = None
    business_address: str | None = None
    trade_license: str | None = None


class MerchantResponse(MerchantBase):
    id: int
    user_id: int
    created_at: datetime
    user: UserResponse

    model_config = ConfigDict(from_attributes=True)