from fastapi import FastAPI
from app.config.settings import settings
from app.hotels.router import router as hotels_router
from app.bookings.router import router as bookings_router

app = FastAPI(title=settings.app.title)

app.include_router(hotels_router)
app.include_router(bookings_router)


# from sqlalchemy import text
# from app.database.engine import engine
#
# @app.get("/test-db")
# async def test_db():
#     async with engine.connect() as conn:
#         result = await conn.execute(text("SELECT 1"))
#         tables = await conn.execute(text(
#             "SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'"
#         ))
#         return {
#             "status": "ok",
#             "tables": [row[0] for row in tables]
#         }