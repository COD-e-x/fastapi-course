from datetime import date
from pydantic import BaseModel, Field


class SHotel(BaseModel):
    address: str
    name: str
    date_from: date
    date_to: date
    has_spa: bool | None = None
    stars: int | None = Field(default=None, ge=1, le=5)


class SHotelsSearch(BaseModel):
    location: str
    name: str
    date_from: date
    date_to: date
    has_spa: bool | None = None
    stars: int | None = Field(default=None, ge=1, le=5)
