from ..models import Product
from subscription.repository.user_subscription import UserSubscriptionRepository


class UserSubscriptionService:

    def __init__(self, repository: UserSubscriptionRepository):
        self._repository = repository

    def get_user_subscription(self, user_id: int) -> Product:
        return self._repository.get_user_subscription(user_id=user_id)
