from sqlalchemy import text
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase
from config import url

engine = create_async_engine(url)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass


async def get_async_session():
    async with async_session_maker() as session:
        yield session

async def create_tables():
    async with engine.begin() as conn:
       await conn.run_sync(Base.metadata.create_all)

async def delete_tables():
   async with engine.begin() as conn:
       await conn.run_sync(Base.metadata.drop_all)

async def check_connect():
    async with async_session_maker() as session:
        try:
            await session.execute(text("SELECT 1"))
            print('\n\n----------- Connection successful !')
        except Exception as e:
            print('\n\n----------- Connection failed ! ERROR : ', e)

