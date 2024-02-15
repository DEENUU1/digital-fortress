from core.repository.base_repository import CRUDRepository
from ..models import UserAccount


class UserAccountRepository(CRUDRepository):

    def __init__(self):
        super().__init__(UserAccount)

    def update_openai_api_key(self, user_id: int, data):
        obj = self.get_by_id(user_id)
        obj.openai_key = data.get("openai_key", None)
        obj.save()
        return obj

