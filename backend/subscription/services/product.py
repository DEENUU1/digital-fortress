from ..models import Product
from subscription.repository.product import ProductRepository
from typing import List, Optional


class ProductService:

    def __init__(self, repository: ProductRepository):
        self._repository = repository

    def get_by_id(self, id: int) -> Optional[Product]:
        return self._repository.get_by_id(id)

    def get_all(self) -> List[Product]:
        return self._repository.get_all()
