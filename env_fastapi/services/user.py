from sqlalchemy.ext.asyncio import AsyncSession

from env_fastapi.dto.user import UserDto
from env_fastapi.models.user import User


async def create_user(data: UserDto, session: AsyncSession):
    user = User(name=data.name)
    try:
        session.add(user)
        await session.commit()
        await session.refresh(user)
    except Exception as e:
        print(e)

    return user


async def get_user(id: int, session: AsyncSession):
    return session.query(User).filter(User.id==id).first()


async def update_user(data: UserDto, session: AsyncSession, id: int):
    user = await get_user(id, session)
    user.name = data.name
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user
