from user.repository.user import UserAccountRepository
from typing import Dict
from ..serializers import (
    OutputUserAccountSerializer,
    InputCreateUserAccountSerializer,
    InputUpdateUserAccountSerializer
)


class UserAccountService:

    def __init__(self, repository: UserAccountRepository):
        self._repository = repository

    def get(self, user_id: int) -> Dict:
        user = self._repository.get_by_id(_id=user_id)
        serializer = OutputUserAccountSerializer(user)
        return serializer.data

    def update(self, user_id: int, request) -> Dict:
        serializer = InputUpdateUserAccountSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.data

        user = self._repository.update(_id=user_id, data=data)
        serializer = OutputUserAccountSerializer(user)
        return serializer.data

    def create(self, request) -> Dict:
        serializer = InputCreateUserAccountSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.data

        user = self._repository.create(data)
        serializer = OutputUserAccountSerializer(user)
        return serializer.data
