from datetime import datetime
from pydantic import BaseModel, ConfigDict
from app.modules.driver.driver_model import DriverStatus, VehicleType
from app.modules.user.user_schema import UserResponse


class DriverBase(BaseModel):
    license_number: str | None = None
    vehicle_type: VehicleType | None = None
    vehicle_number: str | None = None


class DriverCreate(DriverBase):
    user_id: int


class DriverUpdate(BaseModel):
    license_number: str | None = None
    vehicle_type: VehicleType | None = None
    vehicle_number: str | None = None
    status: DriverStatus | None = None


class DriverResponse(DriverBase):
    id: int
    user_id: int
    status: DriverStatus
    current_latitude: float | None = None
    current_longitude: float | None = None
    created_at: datetime
    user: UserResponse

    model_config = ConfigDict(from_attributes=True)