from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.config.database import get_db
from app.modules.driver.driver_schema import DriverCreate
from app.modules.driver.driver_service import create_driver_service

router = APIRouter(
    prefix= "/driver",
    tags= ["Driver"]
)

@router.post("/")
def create_driver_route(
    driver: DriverCreate,
    db: Session = Depends(get_db)
):
    return create_driver_service(driver, db)