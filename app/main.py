from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from app.routes.main import router
from app.config.database import Base, engine
from app.modules.user.user_model import User


Base.metadata.create_all(bind=engine)
from app.core.api_error import ApiError

app = FastAPI()

app.include_router(router)

@app.exception_handler(ApiError)
async def api_error_handler(request: Request, exc: ApiError):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "status_code": exc.status_code,
            "message": exc.message,
        },
    )