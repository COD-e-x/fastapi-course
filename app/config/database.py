from pydantic import BaseModel, SecretStr


class DatabaseConfig(BaseModel):
    database: str
    user: str
    password: SecretStr
    host: str
    port: int
    echo: bool = False

    @property
    def database_url(self) -> str:
        return (
            f"postgresql+asyncpg://{self.user}:{self.password.get_secret_value()}"
            f"@{self.host}:{self.port}/{self.database}"
        )
