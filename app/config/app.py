from pydantic import BaseModel


class AppConfig(BaseModel):
    title: str = "fastapi-course"
    host: str = "127.0.0.1"
    port: int = 8000
