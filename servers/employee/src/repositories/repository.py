from typing import TypeVar, Type, Optional
from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

T = TypeVar("T")


class Repository:
    def __init__(self, model: Type[T]):
        self.model = model

    async def get_all(self, session: AsyncSession) -> list[T]:
        result = await session.execute(select(self.model))
        return list(result.scalars().all())

    async def get_by_id(self, session: AsyncSession, id_: int) -> Optional[T]:
        result = await session.execute(select(self.model).where(self.model.id == id_))  # type: ignore
        return result.scalars().first()

    async def add(self, session: AsyncSession, entity: T) -> T:
        session.add(entity)
        await session.commit()
        await session.refresh(entity)
        return entity

    async def update(self, session: AsyncSession, entity: T) -> T:
        await session.merge(entity)
        await session.commit()
        await session.refresh(entity)
        return entity

    async def delete_by_id(self, session: AsyncSession, id_: int) -> bool:
        result = await session.execute(delete(self.model).where(self.model.id == id_))  # type: ignore
        await session.commit()
        return result.rowcount > 0  # type: ignore

    async def delete_all(self, session: AsyncSession) -> int:
        result = await session.execute(delete(self.model))
        await session.commit()
        return result.rowcount  # type: ignore
