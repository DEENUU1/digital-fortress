from utils.slug_transformer import SlugTransformer
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Project
from subscription.repository.user_subscription import UserSubscriptionRepository


@receiver(post_save, sender=Project)
def create_slug(sender, instance, created, **kwargs):
    if created:
        transformed_title = SlugTransformer.transform(instance.title)
        instance.slug = f"{instance.id}-{transformed_title}"
        instance.save()


@receiver(post_save, sender=Project)
def set_limit_storage(sender, instance, created, **kwargs):
    if created:
        user_product = UserSubscriptionRepository().get_user_subscription(instance.user.id)
        instance.limit_storage = user_product.max_project_storage
        instance.save()


post_save.connect(create_slug, sender=Project)
post_save.connect(set_limit_storage, sender=Project)
