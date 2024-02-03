from ..models import Product
from typing import Optional, List


class ProductSelector:

    def list(self) -> List[Optional[Product]]:
        return Product.objects.filter(is_active=True)

    def get(self, id: int) -> Optional[Product]:
        return Product.objects.filter(is_active=True, id=id).first()

