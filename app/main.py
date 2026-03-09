from fastapi import FastAPI, Query
from datetime import date
from pydantic import BaseModel, Field

app = FastAPI()


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


@app.get("/hotels")
def get_hotels(search_args: SHotelsSearch = Query()) -> list[SHotel]:
    hotels = [
        SHotel(
            address=search_args.location,
            name=search_args.name,
            date_from=search_args.date_from,
            date_to=search_args.date_to,
            has_spa=search_args.has_spa,
            stars=5,
        )
    ]
    return hotels


class SBooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date


@app.post("/bookings")
def add_bookings(booking: SBooking):
    return {"message": "Бронирование создано", "data": booking}
