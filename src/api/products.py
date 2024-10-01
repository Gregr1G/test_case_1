from fastapi import APIRouter
from src.schemas.products import *
from src.repositories.ProductRepo import ProductRepo

products_router = APIRouter(prefix="/products", tags=["Products"])


@products_router.post("") #ok
async def create_product(product: Product):
    new_product = await ProductRepo().add(product.model_dump())
    return new_product


@products_router.get("/{id}")
async def get_product_by_id(id: int):
    current_product = await ProductRepo().retrive(id=id)
    return current_product


@products_router.put("/{id}")
async def product_update(id: int, product: Product):
    updated_prod = await ProductRepo().update(id=id, data=product.model_dump())

    return updated_prod


@products_router.delete("/{id}")
async def product_delete(id: int):
    await ProductRepo().delete(id=id)
    return {"deleted_id": id}



@products_router.get("") #ok
async def get_product_list():
    prods_list = await ProductRepo().list()
    return {"products": prods_list}