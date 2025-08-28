from database.models.address import Address
from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession


async def get_all_addresses(session: AsyncSession) -> list[Address]:
    result = await session.execute(select(Address))
    return list(result.scalars().all())


async def get_address_by_id(session: AsyncSession, address_id: int) -> Address | None:
    result = await session.execute(select(Address).where(Address.id == address_id))
    return result.scalars().first()


async def get_address_by_user_id(session: AsyncSession, user_id: int) -> Address | None:
    result = await session.execute(select(Address).where(Address.user_id == user_id))
    return result.scalars().first()


async def add_address(
    session: AsyncSession, street: str, city: str, postal_code: str, country: str, user_id: int
) -> None:
    address = Address(
        street=street, city=city, postal_code=postal_code, country=country, user_id=user_id
    )
    session.add(address)
    await session.commit()


async def update_address(
    session: AsyncSession,
    address_id: int,
    street: str = None,
    city: str = None,
    postal_code: str = None,
    country: str = None,
) -> bool:
    address = await get_address_by_id(session, address_id)
    if not address:
        return False

    if street is not None:
        address.street = street
    if city is not None:
        address.city = city
    if postal_code is not None:
        address.postal_code = postal_code
    if country is not None:
        address.country = country

    await session.commit()
    return True


async def delete_address_by_id(session: AsyncSession, address_id: int) -> bool:
    result = await session.execute(delete(Address).where(Address.id == address_id))
    await session.commit()
    return result.rowcount > 0


async def delete_all_addresses(session: AsyncSession) -> int:
    result = await session.execute(delete(Address))
    await session.commit()
    return result.rowcount