from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from app.config.settings import settings

engine = create_async_engine(
    settings.database.database_url,
    echo=settings.database.echo,
    connect_args={"server_settings": {"timezone": "UTC"}},
)
AsyncSessionLocal = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)
