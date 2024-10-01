from src.api.products import products_router
from src.api.orders import orders_router
from fastapi import APIRouter


def get_routers():
    router = APIRouter()
    router.include_router(products_router)
    router.include_router(orders_router)
    return router