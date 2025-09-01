from typing import TypeVar, Type, Optional, Protocol
from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

T = TypeVar("T")


class Repository(Protocol[T]):
    def __init__(self, model: Type[T]):
        self.model = model

    async def get_all(self, session: AsyncSession) -> list[T]:
        result = await session.execute(select(self.model))
        return list(result.scalars().all())

    async def get_by_id(self, session: AsyncSession, id: int) -> Optional[T]:
        result = await session.execute(select(self.model).where(self.model.id == id))
        return result.scalars().first()

    async def add(self, session: AsyncSession, entity: T) -> None:
        session.add(entity)
        await session.commit()

    async def delete_by_id(self, session: AsyncSession, id: int) -> bool:
        result = await session.execute(delete(self.model).where(self.model.id == id))
        await session.commit()
        return result.rowcount > 0

    async def delete_all(self, session: AsyncSession) -> int:
        result = await session.execute(delete(self.model))
        await session.commit()
        return result.rowcount
