from sqlalchemy.ext.asyncio import AsyncSession
from repositories.address_repository import address_repository
from schemas import AddressDto


class AddressService:
    async def get_all_addresses(self, session: AsyncSession) -> list[AddressDto]:
        addresses = await address_repository.get_all(session)
        return [AddressDto.model_validate(addr) for addr in addresses]

    async def get_address_by_id(
        self, session: AsyncSession, address_id: int
    ) -> AddressDto:
        address = await address_repository.get_by_id(session, address_id)
        return AddressDto.model_validate(address) if address else None

    async def create_address(
        self,
        session: AsyncSession,
        street: str,
        city: str,
        postal_code: str,
        country_code: str,
        user_id: int,
    ) -> str:
        await address_repository.create(
            session,
            street=street,
            city=city,
            postal_code=postal_code,
            country_code=country_code,
            user_id=user_id,
        )
        return f"Address '{street}, {city}' added"

    async def update_address(
        self,
        session: AsyncSession,
        address_id: int,
        street: str = None,
        city: str = None,
        postal_code: str = None,
        country_code: str = None,
    ) -> str:
        updated = await address_repository.update_by_id(
            session,
            address_id=address_id,
            street=street,
            city=city,
            postal_code=postal_code,
            country_code=country_code,
        )
        if updated:
            return f"Address ID {address_id} updated"
        return f"Address ID {address_id} not found"

    async def delete_address_by_id(self, session: AsyncSession, address_id: int) -> str:
        deleted = await address_repository.delete_by_id(session, address_id)
        if deleted:
            return f"Address ID {address_id} deleted"
        return f"Address ID {address_id} not found"


address_service = AddressService()
