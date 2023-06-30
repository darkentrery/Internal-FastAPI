from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from env_fastapi.dto.user import UserDto
from env_fastapi.settings import settings, get_session
from env_fastapi.services import user as UserService


router = APIRouter()


class Status(BaseModel):
    status: str = "ok"


# @app.get(settings.main_url)
# async def status():
#     return Status()

@router.post(settings.main_url, tags=["user"])
async def create(data: UserDto, session: AsyncSession = Depends(get_session)):
    return await UserService.create_user(data, session)


@router.get("/{id}", tags=["user"])
async def get(id: int, session: AsyncSession = Depends(get_session)):
    return await UserService.get_user(id, session)


@router.put("/{id}", tags=["user"])
async def put(id: int, data: UserDto, session: AsyncSession = Depends(get_session)):
    return await UserService.update_user(data, session, id)


@router.delete("/{id}", tags=["user"])
async def delete(id: int, session: AsyncSession = Depends(get_session)):
    return await UserService.delete_user(id, session)
