from pydantic import BaseModel
from typing import List
import enum


class OrderItem(BaseModel):
    product_id: int
    count: int


class OrderItemsList(BaseModel):
    items: List[OrderItem]


class OrderItemAdd(BaseModel):
    order_id: int
    product_id: int
    count: int

class OrderStatus(enum.Enum):
    PENDING = "собирается"
    RECEIVED = "отправлен"
    COMPLETED = "доставлен"
