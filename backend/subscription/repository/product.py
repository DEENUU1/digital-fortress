from core.repository.base_repository import CRUDRepository
from ..models import Product
from rest_framework.exceptions import NotFound


class ProductRepository(CRUDRepository):

    def __init__(self):
        super().__init__(Product)

    def get_by_name(self, name: str) -> Product:
        if not self.exists_by_name(name):
            raise NotFound(f"Product with name: {name} not found")

        return self._model.objects.get(name=name)

    def exists_by_name(self, name: str) -> bool:
        return self._model.objects.filter(name=name).exists()
