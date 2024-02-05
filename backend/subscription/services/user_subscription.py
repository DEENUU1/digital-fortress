from subscription.repository.user_subscription import UserSubscriptionRepository
from ..serializers import OutputProductSerializer
from typing import Dict


class UserSubscriptionService:

    def __init__(self, repository: UserSubscriptionRepository):
        self._repository = repository

    def get_user_subscription(self, user_id: int) -> Dict:
        user_product = self._repository.get_user_subscription(user_id=user_id)
        serializer = OutputProductSerializer(user_product)
        return serializer.data
