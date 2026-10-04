from fastapi import APIRouter

from app.modules.user.user_routes import router as user_router
from app.modules.auth.auth_routes import router as auth_router

router = APIRouter()

router.include_router(user_router)
router.include_router(auth_router)