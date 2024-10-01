import pytest
from httpx import AsyncClient


import pytest
from sqlalchemy import insert, select

from src.repositories.ProductRepo import ProductRepo
from conftest import client, async_session_maker
from src.models.product_model import Product


@pytest.mark.asyncio
async def test_add_role():
    async with async_session_maker() as session:
        stmt = insert(Product).values(**{
  "title": "string",
  "description": "string",
  "price": 0,
  "count": 0
}).returning(Product)
        result = await session.execute(stmt)
        await session.commit()
        print(result)
        assert result.scalar_one()





# @pytest.mark.asyncio
# async def test_add_specific_operations(ac: AsyncClient):
#     response = await ac.post("/products", json={
#     "title": "string",
#     "description": "string",
#     "price": 100,
#     "count": 10
#     })
#
#     assert response.status_code == 200
#
#
# @pytest.mark.asyncio
# async def test_get_specific_operations(ac: AsyncClient):
#     response = await ac.get("/products")
#
#     assert response.status_code == 200
#     assert len(response.json()["data"]) == 1