from user.repository.user import UserAccountRepository
from typing import Dict


class UserAccountService:

    def __init__(self, repository: UserAccountRepository):
        self._repository = repository

    def get(self, user_id: int) -> Dict:
        return self._repository.get_by_id(_id=user_id)

    def update(self, user_id: int, data) -> Dict:
        return self._repository.update(_id=user_id, data=data)

    def create(self, data) -> Dict:
        return self._repository.create(data)
