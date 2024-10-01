from sqlalchemy.orm import Mapped, mapped_column

from src.database.databse import Base
from typing import Optional



class Product(Base):
    __tablename__ = "product"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    description: Mapped[Optional[str]]
    price: Mapped[int]
    count: Mapped[int]

    def UpdateData(self, attrs: dict):
        for attr, value in attrs.items():
            setattr(self, attr, value)
