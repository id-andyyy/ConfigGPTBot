from sqlalchemy import select
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, async_sessionmaker

from config_data.config import load_config, Config
from models.models import User, Role

config: Config = load_config(r'.env')
engine: AsyncEngine = create_async_engine(f'sqlite+aiosqlite:///{config.db.db_name}.db')
async_session = async_sessionmaker(engine, expire_on_commit=False)


async def add_user(tg_id: int) -> None:
    async with async_session() as session:
        async with session.begin():
            result = await session.execute(select(Role).where(Role.id == 1))
            role_user = result.scalars().one()
            user: User = User(tg_id=tg_id, role=role_user)
            session.add(user)


async def get_info() -> None:
    async with async_session() as session:
        async with session.begin():
            result = await session.execute(select(Role).all())
            print(result.fetchall())
