from sqlalchemy import Boolean, Integer, String, Column
from env_fastapi.settings import settings


class User(settings.Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)