from core.repository.base_repository import CRUDRepository
from ..models import Product


class ProductRepository(CRUDRepository):

    def __init__(self):
        super().__init__(Product)
