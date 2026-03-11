from fastapi import APIRouter, Query
from app.hotels.schemas import SHotel, SHotelsSearch

router = APIRouter(prefix="/hotels", tags=["Hotels"])


@router.get("")
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
