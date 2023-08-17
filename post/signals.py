from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import Post


@receiver(pre_save, sender=Post)
def update_number_like(sender, instance, created, **kwargs):
    post_like = instance.like
