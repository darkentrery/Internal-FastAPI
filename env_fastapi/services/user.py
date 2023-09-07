from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession

from env_fastapi.dto.user import UserGetDto
from env_fastapi.models.user import User


async def create_user(data: UserGetDto, session: AsyncSession):
    user = User(name=data.name)
    try:
        session.add(user)
        await session.commit()
        await session.refresh(user)
    except Exception as e:
        print(e)

    return user


async def get_user(id: int, session: AsyncSession):
    result = await session.execute(select(User).where(User.id == id))
    return result.scalar()


async def update_user(data: UserGetDto, session: AsyncSession, id: int):
    user = await get_user(id, session)
    user.name = data.name
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user


async def delete_user(id: int, session: AsyncSession):
    user = await session.execute(delete(User).where(User.id==id))
    await session.commit()
    return user
