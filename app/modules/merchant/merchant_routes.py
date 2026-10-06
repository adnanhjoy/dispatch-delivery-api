from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.config.database import get_db
from .merchant_schema import MerchantCreate
from .merchant_service import create_merchant_service

router = APIRouter(
    prefix= "/merchant",
    tags= ["Merchant"]
)

@router.post("/")
def create_merchant_route(
    merchant: MerchantCreate,
    db: Session = Depends(get_db)
):
    return create_merchant_service(merchant, db)