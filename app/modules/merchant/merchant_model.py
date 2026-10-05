from datetime import datetime, timezone

from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.config.database import Base

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.modules.user.user_model import User
class MerchantProfile(Base):
    __tablename__ = "merchant_profiles"

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

    business_name: Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )

    business_phone: Mapped[str | None] = mapped_column(
        String(20),
        nullable=True
    )

    business_address: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    trade_license: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        default=datetime.now(timezone.utc),
        nullable=False
    )

    user: Mapped["User"] = relationship(
        "User",
        back_populates="merchant_profile"
    )