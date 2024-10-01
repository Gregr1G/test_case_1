from src.utils.repository import BaseRepo
from src.models.product_model import Product

class ProductRepo(BaseRepo):
    model = Product


