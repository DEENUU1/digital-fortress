from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserAccount
from subscription.models import Product, UserSubscription


@receiver(post_save, sender=UserAccount)
def create_user_subscription(sender, instance, created, **kwargs):
    if created:
        pass


post_save.connect(create_user_subscription, sender=UserAccount)
