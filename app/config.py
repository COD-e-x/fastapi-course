from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application configuration loaded from environment variables (.env).
    """

    db_database: str
    db_user: str
    db_password: str
    db_host: str
    db_port: int
    db_echo: bool = False

    model_config = SettingsConfigDict(env_file=".env")

    @property
    def database_url(self) -> str:
        """Return SQLAlchemy database URL."""
        return (
            f"postgresql+asyncpg://{self.db_user}:{self.db_password}"
            f"@{self.db_host}:{self.db_port}/{self.db_database}"
        )


settings = Settings()
