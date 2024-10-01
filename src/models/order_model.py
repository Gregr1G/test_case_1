from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column

from src.database.databse import Base

from datetime import datetime



class OrderItem(Base):
    __tablename__ = "order_item"

    id: Mapped[int] = mapped_column(primary_key=True)
    order_id: Mapped[int] = mapped_column(ForeignKey("order.id"))
    product_id: Mapped[int] = mapped_column(ForeignKey("product.id"))
    count: Mapped[int]


class Order(Base):
    __tablename__ = "order"

    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[datetime] = mapped_column(default=func.now())
    status: Mapped[str] = mapped_column(default="собирается")