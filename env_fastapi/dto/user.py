from pydantic import BaseModel
from fastapi_users import schemas


class UserGetDto(schemas.BaseUser[int]):
    name: str
    created: str


class UserCreateDTO(schemas.BaseUserCreate):
    name: str
    created: str
