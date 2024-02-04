from core.repository.base_repository import CRUDRepository
from ..models import UserAccount


class UserAccountRepository(CRUDRepository):

    def __init__(self):
        super().__init__(UserAccount)
