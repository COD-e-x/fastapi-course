from pydantic_settings import BaseSettings, SettingsConfigDict
from app.config.app import AppConfig
from app.config.database import DatabaseConfig


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="APP__",
        env_nested_delimiter="__",
        env_file=(".env.example", ".env"),
        env_file_encoding="utf-8",
    )
    app: AppConfig = AppConfig()
    database: DatabaseConfig


settings = Settings()
