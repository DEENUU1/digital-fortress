from ..models import Product
from typing import Optional, List
from rest_framework import exceptions


class ProductSelector:

    def list(self) -> List[Optional[Product]]:
        return Product.objects.filter(is_active=True)

    def get(self, id: int) -> Optional[Product]:
        exists = Product.objects.filter(is_active=True, id=id).exists()
        if not exists:
            raise exceptions.NotFound(f"Product with id {id} not found")
        return Product.objects.filter(is_active=True, id=id).first()

