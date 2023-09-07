import uuid

from fastapi import APIRouter, Depends
from fastapi_users import FastAPIUsers
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from env_fastapi.dto.user import UserGetDto
from env_fastapi.models.user import User
from env_fastapi.services.auth import auth_backend
from env_fastapi.services.user_manager import get_user_manager
from env_fastapi.settings import settings, get_session
from env_fastapi.services import user as UserService


router = APIRouter()

fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [auth_backend],
)

current_user = fastapi_users.current_user()


class Status(BaseModel):
    status: str = "ok"


# @app.get(settings.main_url)
# async def status():
#     return Status()

@router.post(settings.main_url, tags=["user"])
async def create(data: UserGetDto, session: AsyncSession = Depends(get_session)):
    return await UserService.create_user(data, session)


@router.get("/{id}", tags=["user"])
async def get(id: int, session: AsyncSession = Depends(get_session), user: User = Depends(current_user)):
    return await UserService.get_user(id, session)


@router.put("/{id}", tags=["user"])
async def put(id: int, data: UserGetDto, session: AsyncSession = Depends(get_session)):
    return await UserService.update_user(data, session, id)


@router.delete("/{id}", tags=["user"])
async def delete(id: int, session: AsyncSession = Depends(get_session)):
    return await UserService.delete_user(id, session)
