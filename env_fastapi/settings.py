import os

from dotenv import load_dotenv
from pydantic import BaseSettings

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker


class Settings(BaseSettings):
    main_url: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_NAME: str
    POSTGRES_HOST: str
    POSTGRES_PORT: str

    @property
    def SQLALCHEMY_DATABASE_URL(self):
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_NAME}"

    @property
    def engine(self):
        return create_async_engine(self.SQLALCHEMY_DATABASE_URL, echo=True)

    @property
    def Base(self):
        return declarative_base()

    @property
    def async_session(self):
        return sessionmaker(bind=self.engine, class_=AsyncSession, expire_on_commit=False, autoflush=False)


dotenv_path = os.path.join(os.path.dirname(__file__), "../.env")
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


# POSTGRES_USER = environ.get("POSTGRES_USER", "postgres")
# POSTGRES_PASSWORD = environ.get("POSTGRES_PASSWORD", "postgres")
# POSTGRES_NAME = environ.get("POSTGRES_NAME", "postgres")
# POSTGRES_HOST = environ.get("POSTGRES_HOST", "localhost")

# SQLALCHEMY_DATABASE_URL = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:5437/{POSTGRES_NAME}"
# engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)
# Base = declarative_base()
# async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


settings = Settings()

Base = declarative_base()


async def init_models():
    async with settings.engine.begin() as conn:
        await conn.run_sync(settings.Base.metadata.drop_all)
        await conn.run_sync(settings.Base.metadata.create_all)


async def get_session() -> AsyncSession:
    async with settings.async_session() as session:
        yield session
