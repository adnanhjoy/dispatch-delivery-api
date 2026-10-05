from datetime import datetime, timezone
from enum import Enum
from sqlalchemy import String, Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.config.database import Base

from app.modules.customer.customer_model import CustomerProfile
from app.modules.driver.driver_model import DriverProfile
from app.modules.merchant.merchant_model import MerchantProfile

class UserRole(str, Enum):
    ADMIN = "admin"
    MERCHANT = "merchant"
    DRIVER = "driver"
    CUSTOMER = "customer"

class UserStatus(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    SUSPENDED = "suspended"

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        index=True,
        nullable=False
    )

    phone: Mapped[str | None] = mapped_column(
        String(20),
        unique=True,
        index=True,
        nullable=True
    )

    password: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    role: Mapped[UserRole] = mapped_column(
        SQLEnum(UserRole),
        default=UserRole.CUSTOMER,
        nullable=False,
        index=True
    )

    status: Mapped[UserStatus] = mapped_column(
        SQLEnum(UserStatus),
        default=UserStatus.ACTIVE,
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        default=datetime.now(timezone.utc),
        nullable=False
    )

    updated_at: Mapped[datetime] = mapped_column(
        default=datetime.now(timezone.utc),
        onupdate=datetime.now(timezone.utc),
        nullable=False
    )

    merchant_profile: Mapped["MerchantProfile | None"] = relationship(
        MerchantProfile,
        back_populates="user",
        uselist=False
    )

    driver_profile: Mapped["DriverProfile | None"] = relationship(
        "DriverProfile",
        back_populates="user",
        uselist=False
    )

    customer_profile: Mapped["CustomerProfile | None"] = relationship(
        "CustomerProfile",
        back_populates="user",
        uselist=False
    )