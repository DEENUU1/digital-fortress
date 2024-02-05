from core.repository.base_repository import CRUDRepository
from ..models import ProductPrice


class ProductPriceRepository(CRUDRepository):

    def __init__(self):
        super().__init__(ProductPrice)

    def price_exists(self, value: float, currency: str) -> bool:
        return self._model.objects.filter(value=value, currency=currency).exists()
