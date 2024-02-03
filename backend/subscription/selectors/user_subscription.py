from ..models import UserSubscription
from typing import Optional


class UserSubscriptionSelector:

    def get(self, user_id: int) -> Optional[UserSubscription]:
        return UserSubscription.objects.filter(user_id=user_id).first()
