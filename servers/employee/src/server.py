import logging
from asyncio import CancelledError
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from dataclasses import dataclass
from typing import Optional

from faker import Faker

from config import settings
from connect import Database
from models import Base, User, Address, WorkStatus
from mcp.server.fastmcp import Context, FastMCP
from mcp.server.session import ServerSession
from schemas import Gender, UserDto, AddressDto
from validation import CreateUserRequest, UpdateUserRequest
from services.user_service import user_service
from services.address_service import address_service
from pydantic import ValidationError

logger = logging.getLogger(__name__)


@dataclass
class AppContext:
    db: Database


@asynccontextmanager
async def server_lifespan(server: FastMCP) -> AsyncIterator[AppContext]:
    db = await Database.connect()
    logger.info("✅ Database connected")

    async with db.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    logger.info("✅ Tables created")

    # await _setup(db)

    try:
        yield AppContext(db=db)
    except (CancelledError, Exception):
        logger.warning("⚠️ Server interrupted")

        # await _cleanup(db)

        await db.disconnect()
        logger.info("✅ Database disconnected")


async def _setup(db: "Database"):
    async with db.get_async_session() as session:
        fake = Faker()
        users = [
            User(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.email(),
                age=fake.random_int(18, 80),
                gender=fake.random_element([Gender.MALE, Gender.FEMALE, Gender.OTHER]),
                address=Address(
                    street=fake.street_address(),
                    city=fake.city(),
                    postal_code=fake.postcode(),
                    country_code=fake.country_code(),
                ),
                work_status=WorkStatus(is_home_office=fake.boolean()),
            )
            for _ in range(settings.initial_users_count)
        ]
        session.add_all(users)
        await session.commit()
    logger.info(f"✅ {len(users)} users added")


async def _cleanup(db: "Database"):
    try:
        async with db.engine.begin() as conn:
            await conn.run_sync(User.metadata.drop_all)
            logger.info("✅ Tables dropped")
    except (CancelledError, Exception):
        pass


mcp = FastMCP("Employee Database Demo", lifespan=server_lifespan)


def _get_db(ctx: Context[ServerSession, AppContext]) -> Database:
    return ctx.request_context.lifespan_context.db


@mcp.tool(name="Find all users", description="Get all users from database.")
async def find_all_users(ctx: Context[ServerSession, AppContext]) -> list[UserDto]:
    async with _get_db(ctx).get_async_session() as session:
        return await user_service.get_all_users(session)


@mcp.tool(name="Find user by last name", description="Get an user by name.")
async def find_user_by_last_name(
    ctx: Context[ServerSession, AppContext], name: str
) -> UserDto | None:
    async with _get_db(ctx).get_async_session() as session:
        return await user_service.get_user_by_last_name(session, name)


@mcp.tool(
    name="Add a user",
    description="Add a user with name, email, age and gender "
    "(male/female/other) to the database.",
)
async def add_user(
    ctx: Context[ServerSession, AppContext],
    first_name: str,
    last_name: str,
    email: str,
    age: int,
    gender: Optional[Gender] = None,
) -> str:
    try:
        request = CreateUserRequest(
            first_name=first_name,
            last_name=last_name,
            email=email,
            age=age,
            gender=gender,
        )
        async with _get_db(ctx).get_async_session() as session:
            result = await user_service.create_user(
                session,
                request.first_name,
                request.last_name,
                request.email,
                request.age,
                request.gender,
            )
            logger.info(f"✅ {result}")
            return result
    except (ValidationError, ValueError) as e:
        logger.error(str(e))
        return str(e)


@mcp.tool(
    name="Update user",
    description="Update a user by last name with optional new values. "
    "Gender options: male/female/other.",
)
async def update_user(
    ctx: Context[ServerSession, AppContext],
    last_name: str,
    first_name: Optional[str] = None,
    email: Optional[str] = None,
    age: Optional[int] = None,
    gender: Optional[Gender] = None,
) -> str:
    try:
        request = UpdateUserRequest(
            last_name=last_name,
            first_name=first_name,
            email=email,
            age=age,
            gender=gender,
        )
        async with _get_db(ctx).get_async_session() as session:
            result = await user_service.update_user(
                session,
                request.last_name,
                request.first_name,
                request.email,
                request.age,
                request.gender,
            )
            if "updated" in result:
                logger.info(f"✅ {result}")
            else:
                logger.warning(f"⚠️ {result}")
            return result
    except (ValidationError, ValueError) as e:
        logger.error(str(e))
        return str(e)


@mcp.tool(
    name="Delete user by last name",
    description="Delete a user by last name from the database.",
)
async def delete_user_by_last_name(
    ctx: Context[ServerSession, AppContext], last_name: str
) -> str:
    async with _get_db(ctx).get_async_session() as session:
        result = await user_service.delete_user_by_last_name(session, last_name)
        if "deleted" in result:
            logger.info(f"✅ {result}")
        else:
            logger.warning(f"⚠️ {result}")
        return result


@mcp.tool(name="Delete all users", description="Deletes all users from the database.")
async def delete_all_users(ctx: Context[ServerSession, AppContext]) -> str:
    async with _get_db(ctx).get_async_session() as session:
        result = await user_service.delete_all_users(session)
        logger.info(f"✅ {result}")
        return result


@mcp.tool(name="Find all addresses", description="Get all addresses from database.")
async def find_all_addresses(
    ctx: Context[ServerSession, AppContext],
) -> list[AddressDto]:
    async with _get_db(ctx).get_async_session() as session:
        return await address_service.get_all_addresses(session)


@mcp.tool(name="Find address by ID", description="Get address by ID.")
async def find_address_by_id(
    ctx: Context[ServerSession, AppContext], address_id: int
) -> AddressDto | None:
    async with _get_db(ctx).get_async_session() as session:
        return await address_service.get_address_by_id(session, address_id)


@mcp.tool(
    name="Add address",
    description="Add a new address to the database. Use ISO 3166-1 alpha-2 "
    "country code (e.g., 'DE', 'US', 'FR').",
)
async def add_address(
    ctx: Context[ServerSession, AppContext],
    street: str,
    city: str,
    postal_code: str,
    country_code: str,
    user_id: int,
) -> str:
    try:
        async with _get_db(ctx).get_async_session() as session:
            result = await address_service.create_address(
                session, street, city, postal_code, country_code, user_id
            )
            logger.info(f"✅ {result}")
            return result
    except ValueError as e:
        logger.error(str(e))
        return str(e)


@mcp.tool(
    name="Update address",
    description="Update an address by ID. Use ISO 3166-1 alpha-2 "
    "country code (e.g., 'DE', 'US', 'FR').",
)
async def update_address(
    ctx: Context[ServerSession, AppContext],
    address_id: int,
    street: str = None,
    city: str = None,
    postal_code: str = None,
    country_code: str = None,
) -> str:
    try:
        async with _get_db(ctx).get_async_session() as session:
            result = await address_service.update_address(
                session, address_id, street, city, postal_code, country_code
            )
            if "updated" in result:
                logger.info(f"✅ {result}")
            else:
                logger.warning(f"⚠️ {result}")
            return result
    except ValueError as e:
        logger.error(str(e))
        return str(e)


@mcp.tool(name="Delete address by ID", description="Delete an address by ID.")
async def delete_address_by_id(
    ctx: Context[ServerSession, AppContext], address_id: int
) -> str:
    async with _get_db(ctx).get_async_session() as session:
        result = await address_service.delete_address_by_id(session, address_id)
        if "deleted" in result:
            logger.info(f"✅ {result}")
        else:
            logger.warning(f"⚠️ {result}")
        return result


@mcp.prompt("zeige-mitarbeiter-anzahl")
async def get_number_of_employees():
    return """Wie viele Mitarbeiter sind aktuell in der Datenbank gespeichert?
    Zeige das Ergebnis zunächst sortiert nach Länderkennung und die dann die
    Gesamtzahl aller Mitarbeiter!
    """


@mcp.prompt("zeige-mitarbeiter")
async def list_employees() -> str:
    return """Gib eine Liste aller Mitarbeiter zurück, die in der Datenbank
    gespeichert sind!

    1. Hole zunächst alle Mitarbeiter mit ihrer Adresse aus der Datenbank.
    2. Formatiere das Ergebnis, so dass pro Mitarbeiter eine Zeile angezeigt
       wird und tenne die einzelnen Daten durch Komma voneinander.
    3. Stelle jeder Zeile eine fortlaufende Nummer voran, die rechtsbündig
       ausgerichtet ist.
       """


@mcp.prompt("erzeuge-mitarbeiter")
def employee_database_populate(anzahl: int, land: str):
    return f"""Füge {anzahl} Mitarbeiter in die Mitarbeiter-Datenbank ein,
    die ihren Wohnsitz ausschliesslich in {land} haben!
    """
