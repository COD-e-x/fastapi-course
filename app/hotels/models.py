from sqlalchemy import (
    String,
    JSON,
)
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import (
    Base,
)
from app.database.annotations import intpk, created_at, updated_at


class Hotels(Base):
    __tablename__ = "hotels"

    id: Mapped[intpk]
    name: Mapped[str] = mapped_column(String(255))
    location: Mapped[str] = mapped_column(String(255))
    services: Mapped[dict | None] = mapped_column(JSON)
    rooms_quantity: Mapped[int]
    image_id: Mapped[int | None]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
