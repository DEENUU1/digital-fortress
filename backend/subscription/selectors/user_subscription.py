from ..models import UserSubscription


class UserSubscriptionSelector:

    def get(self, user_id: int) -> UserSubscription:
        return UserSubscription.objects.filter(user_id=user_id).first()
