from core.repository.base_repository import CRUDRepository
from ..models import UserAccount


class UserAccountRepository(CRUDRepository):

    def __init__(self):
        super().__init__(UserAccount)

    def set_openai_key(self, value: str, user_id: int) -> UserAccount:
        user = self.get_by_id(user_id)
        user.openai_key = value
        user.save()
        return user
