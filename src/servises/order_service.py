from src.repositories.ProductRepo import ProductRepo
from src.models.product_model import Product
import asyncio


async def CountSubtractionService(id: int, count: int, prod_count: int):
    await ProductRepo().update(id=id, data={"count": prod_count - count})


async def ProductService(id: int, count: int):
    product = await ProductRepo().retrive(id=id)
    if product.count >= count:
        return product.count
    return False

