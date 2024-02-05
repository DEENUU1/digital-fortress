from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserAccount, Product, ProductPrice
from subscription.models import Product, UserSubscription
from subscription.repository.product import ProductRepository
from subscription.repository.user_subscription import UserSubscriptionRepository
from datetime import datetime, timedelta
from subscription.services.product import ProductService


@receiver(post_save, sender=UserAccount)
def create_new_user_subscription(sender, instance, created, **kwargs):
    if created:
        free_product = ProductRepository().get_product_with_zero_price()
        if not free_product:
            free_product = ProductService(ProductRepository()).create_free_product()

        user_subscription = UserSubscriptionRepository().create({
            "user": instance,
            "product": free_product,
            "expiration_date": datetime.now() + timedelta(weeks=999)
        })
        user_subscription.save()


post_save.connect(create_new_user_subscription, sender=UserAccount)
