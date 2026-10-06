
import logging

from sqlalchemy.orm import Session
from .merchant_model import MerchantProfile
from app.core.api_error import ApiError
from .merchant_schema import MerchantCreate

def create_merchant_service(merchant_data: MerchantCreate, db: Session):
    logging.info(merchant_data)
    is_exist = db.query(MerchantProfile).filter(
            MerchantProfile.user_id == merchant_data.user_id
        ).first()
    
    if is_exist:
        raise ApiError(400, "Merchant already exists")
    new_merchant = MerchantProfile(**merchant_data.model_dump())
    db.add(new_merchant)
    db.commit()
    db.refresh(new_merchant)
    return new_merchant