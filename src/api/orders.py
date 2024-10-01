from fastapi import APIRouter, HTTPException
from src.repositories.OrderRepo import OrderRepo, OrderItemsRepo
from src.servises.order_service import ProductService, CountSubtractionService
from src.schemas.orders import *

orders_router = APIRouter(prefix="/orders", tags=["Orders"])


@orders_router.post("")
async def create_order(products: OrderItemsList):
    items = []

    for product_id, count in products.items:

        valide = await ProductService(id=product_id[1], count=count[1])
        if not valide:
            raise HTTPException(status_code=400,
                                detail=f"На складе нет столько товара c id {product_id[1]}. Имеющееся колличество {count[1]}")
        items.append([product_id[1], count[1], valide])

    order = await OrderRepo().add_without_args()

    for product_id, count, prod_count in items:
            new_item = OrderItemAdd(order_id=order.id, product_id=product_id, count=count)
            await CountSubtractionService(id=product_id, count=count, prod_count=prod_count)
            await OrderItemsRepo().add(new_item.model_dump())

    return order


@orders_router.get("")
async def get_orders():
    orders = await OrderRepo().list()
    return orders


@orders_router.get("/{id}")
async def get_order_by_id(id: int):
    order = await OrderRepo().retrive(id=id)
    order_items = await OrderItemsRepo().list_by_order_id(id=id)
    return {"order": order, "items": order_items}


@orders_router.patch("/{id}/{status}")
async def change_status(id: int, status: OrderStatus):
    updated_order = await OrderRepo().update(id=id, data={"status": status.value})
    return updated_order