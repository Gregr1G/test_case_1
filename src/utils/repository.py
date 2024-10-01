from abc import ABC, abstractmethod

from sqlalchemy import insert, select

from src.database.databse import async_session_maker

class AbstractRepo(ABC):
    @abstractmethod
    async def add(self, data: dict):
        pass

    @abstractmethod
    async def delete(self, id: int):
        pass

    @abstractmethod
    async def retrive(self, id: int):
        pass

    @abstractmethod
    async def list(self):
        pass

    @abstractmethod
    async def update(self, id: int, data: dict):
        pass


class BaseRepo(AbstractRepo):
    model = None

    async def add(self, data: dict):
        async with async_session_maker() as session:
            stmt = insert(self.model).values(**data).returning(self.model)
            result = await session.execute(stmt)
            await session.commit()
            return result.scalar_one()

    async def add_without_args(self):
        async with async_session_maker() as session:
            obj = self.model()
            session.add(obj)

            await session.commit()
            return obj

    async def list(self):
        async with async_session_maker() as session:
            stmt = select(self.model)
            res = await session.execute(stmt)
            return res.scalars().all()

    async def list_by_order_id(self, id: int):
        async with async_session_maker() as session:
            stmt = select(self.model).where(self.model.order_id == id)
            res = await session.execute(stmt)
            return res.scalars().all()

    async def retrive(self, id: int):
        async with async_session_maker() as session:
            result = await session.execute(select(self.model).where(self.model.id == id))
            return result.scalars().one()

    async def delete(self, id: int):
        async with async_session_maker() as session:
            result = await session.execute(select(self.model).where(self.model.id == id))
            current_object = result.scalars().first()

            await session.delete(current_object)
            await session.commit()

    async def update(self, id: int, data: dict):
        async with async_session_maker() as session:
            res = await session.execute(select(self.model).where(self.model.id == id))
            current_object = res.scalars().first()

            for key, value in data.items():
                setattr(current_object, key, value)

            await session.commit()
        return current_object