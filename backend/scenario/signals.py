from utils.slug_transformer import SlugTransformer
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Project


@receiver(post_save, sender=Project)
def create_slug(sender, instance, created, **kwargs):
    if created:
        transformed_title = SlugTransformer.transform(instance.title)
        instance.slug = f"{instance.id}-{transformed_title}"


post_save.connect(create_slug, sender=Project)
