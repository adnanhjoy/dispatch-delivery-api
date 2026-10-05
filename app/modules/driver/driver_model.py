from datetime import datetime, timezone
from enum import Enum

from sqlalchemy import ForeignKey, String, Float, Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.config.database import Base

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.modules.user.user_model import User
class DriverStatus(str, Enum):
    AVAILABLE = "available"
    BUSY = "busy"
    OFFLINE = "offline"
    SUSPENDED = "suspended"


class VehicleType(str, Enum):
    BIKE = "bike"
    CAR = "car"
    VAN = "van"
    TRUCK = "truck"


class DriverProfile(Base):
    __tablename__ = "driver_profiles"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        unique=True,
        nullable=False,
        index=True
    )

    license_number: Mapped[str | None] = mapped_column(
        String(100),
        unique=True,
        nullable=True
    )

    vehicle_type: Mapped[VehicleType | None] = mapped_column(
        SQLEnum(VehicleType),
        nullable=True
    )

    vehicle_number: Mapped[str | None] = mapped_column(
        String(50),
        unique=True,
        nullable=True
    )

    status: Mapped[DriverStatus] = mapped_column(
        SQLEnum(DriverStatus),
        default=DriverStatus.OFFLINE,
        nullable=False
    )

    current_latitude: Mapped[float | None] = mapped_column(
        Float,
        nullable=True
    )

    current_longitude: Mapped[float | None] = mapped_column(
        Float,
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        default=datetime.now(timezone.utc),
        nullable=False
    )

    user: Mapped["User"] = relationship(
        back_populates="driver_profile"
    )