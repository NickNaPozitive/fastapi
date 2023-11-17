from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.config import settings


# DATABASE_URL = "postgresql+asyncpg://postgres:nick@localhost:5432/postgres"
# engine = create_async_engine(DATABASE_URL)


engine = create_async_engine(settings.DATABASE_URL)


async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

class Base(DeclarativeBase):
    pass