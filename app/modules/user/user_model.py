from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.config.database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        index=True,
    )
    password: Mapped[str] = mapped_column(String(255))
    status: Mapped[str] = mapped_column(String(255), default="inactive")
    phone: Mapped[str] = mapped_column(String(255))
    address: Mapped[str] = mapped_column(String(255))