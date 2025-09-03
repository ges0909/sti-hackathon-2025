from models.address import Address
from repositories.repository import Repository
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


class AddressRepository(Repository):
    def __init__(self):
        super().__init__(Address)

    async def get_by_user_id(
        self, session: AsyncSession, user_id: int
    ) -> Address | None:
        result = await session.execute(
            select(Address).where(Address.user_id == user_id)
        )
        return result.scalars().first()

    async def create(
        self,
        session: AsyncSession,
        street: str,
        city: str,
        postal_code: str,
        country_code: str,
        user_id: int,
    ) -> None:
        address = Address(
            street=street,
            city=city,
            postal_code=postal_code,
            country_code=country_code,
            user_id=user_id,
        )
        await self.add(session, address)

    async def update_by_id(
        self,
        session: AsyncSession,
        address_id: int,
        street: str = None,
        city: str = None,
        postal_code: str = None,
        country_code: str = None,
    ) -> bool:
        address = await self.get_by_id(session, address_id)
        if not address:
            return False

        if street is not None:
            address.street = street
        if city is not None:
            address.city = city
        if postal_code is not None:
            address.postal_code = postal_code
        if country_code is not None:
            address.country_code = country_code

        await session.commit()
        return True


address_repository = AddressRepository()
