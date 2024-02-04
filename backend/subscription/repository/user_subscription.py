from core.repository.base_repository import CRUDRepository
from ..models import UserSubscription, Product


class UserSubscriptionRepository(CRUDRepository):

    def __init__(self):
        super().__init__(UserSubscription)

    def get_user_subscription(self, user_id: int) -> Product:
        user_subscription = self._model.objects.get(user=user_id)
        product = Product.objects.get(id=user_subscription.product.id)
        return product
