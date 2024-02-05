from ..models import Product
from subscription.repository.product import ProductRepository
from typing import List, Optional, Dict
from ..serializers import OutputProductSerializer


class ProductService:

    def __init__(self, repository: ProductRepository):
        self._repository = repository

    def get_by_id(self, id: int) -> Dict:
        product = self._repository.get_by_id(id)
        serializer = OutputProductSerializer(product)
        return serializer.data

    def get_all(self) -> List[Dict]:
        products = self._repository.get_all()
        serializer = OutputProductSerializer(products, many=True)
        return serializer.data
