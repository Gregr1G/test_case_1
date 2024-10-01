from src.utils.repository import BaseRepo
from src.models.order_model import Order, OrderItem


class OrderRepo(BaseRepo):
    model = Order


class OrderItemsRepo(BaseRepo):
    model = OrderItem