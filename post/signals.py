from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Like, Post


@receiver(post_save, sender=Like)
def update_number_like(sender, instance, created, **kwargs):
    print('signals call', instance.post.id)
    if created:
        post = Post.objects.get(id=instance.post.id)
        print(post)
        post.like_count = post.post_like.count()
        post.save()
