from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Like, Post


@receiver(post_save, sender=Like)
def update_number_like(sender, instance, created, **kwargs):
    if created:
        post = Post.objects.get(id=instance.post.id)
        post.like_count = post.post_like.count()
        post.save()


@receiver(post_delete, sender=Like)
def update_number_like(sender, instance, **kwargs):
    post = Post.objects.get(id=instance.post.id)
    post.like_count = post.post_like.count()
    post.save()
