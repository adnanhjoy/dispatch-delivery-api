from typing import Generic, TypeVar

from pydantic import BaseModel


T = TypeVar("T")


class ApiResponse(BaseModel, Generic[T]):
    success: bool = True
    status_code: int
    message: str
    data: T | None = None