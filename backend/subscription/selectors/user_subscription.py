from ..models import UserSubscription
from user.models import UserAccount


class UserSubscriptionSelector:

    def get(self, user_id: int) -> UserSubscription:
        return UserSubscription.objects.filter(user_id=user_id).first()

    def create_new_user_subscription(self, user: UserAccount) -> UserSubscription:
        pass 