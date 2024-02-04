from utils.slug_transformer import SlugTransformer
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Project


@receiver(pre_save, sender=Project)
def create_slug(sender, instance, **kwargs):
    transformed_title = SlugTransformer.transform(instance.title)
    instance.slug = f"{instance.id}-{transformed_title}"


pre_save.connect(create_slug, sender=Project)
