from sqlalchemy.orm import Session

from app.core.api_error import ApiError
from app.modules.driver.driver_schema import DriverCreate

from .driver_model import DriverProfile


def create_driver_service(driver_data: DriverCreate, db: Session):

    # Check user already has a driver profile
    is_exist = db.query(DriverProfile).filter(
        DriverProfile.user_id == driver_data.user_id
    ).first()

    if is_exist:
        raise ApiError(400, "Driver already exists")

    # Check license number
    license_exist = db.query(DriverProfile).filter(
        DriverProfile.license_number == driver_data.license_number
    ).first()

    if license_exist:
        raise ApiError(400, "Your license number is already used")

    # Check vehicle number
    vehicle_exist = db.query(DriverProfile).filter(
        DriverProfile.vehicle_number == driver_data.vehicle_number
    ).first()

    if vehicle_exist:
        raise ApiError(400, "Your vehicle number is already used")

    new_driver = DriverProfile(**driver_data.model_dump())

    db.add(new_driver)
    db.commit()
    db.refresh(new_driver)

    return new_driver