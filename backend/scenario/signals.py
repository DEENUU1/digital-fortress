from utils.slug_transformer import SlugTransformer
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Project


@receiver(pre_save, sender=Project)
def create_slug(sender, instance, created, **kwargs):
    # Create slug for JobOffer object based on title and id
    if created:
        transformed_title = SlugTransformer.transform(instance.title)
        instance.slug = f"{instance.id}-{transformed_title}"
        instance.save()


pre_save.connect(create_slug, sender=Project)