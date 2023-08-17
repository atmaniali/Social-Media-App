import os
import uuid

from django.utils.deconstruct import deconstructible

from django.db import models


# Create your models here.
@deconstructible
class GenerateImagePostPath(object):
    def __int__(self):
        pass

    def __call__(self, instance, filename):
        ext = filename.split(".")[-1]
        path = f"posts/{instance.author.id}/images/"
        name = f"post_image.{ext}"
        return os.path.join(path, name)


@deconstructible
class GenerateVideoPostPath(object):
    def __int__(self):
        pass

    def __call__(self, instance, filename):
        ext = filename.split(".")[-1]
        path = f"posts/{instance.author.id}/images/"
        name = f"post_video.{ext}"
        return os.path.join(path, name)


post_image = GenerateImagePostPath()
post_video = GenerateVideoPostPath()


class Post(models.Model):
    # id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4())
    author = models.OneToOneField('users.profile', on_delete=models.CASCADE)
    like = models.ForeignKey('users.profile', on_delete=models.SET_NULL, blank=True, null=True,
                             related_name='post_like')
    content = models.TextField()
    like_count = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to=post_image, blank=True, null=True)
    video = models.FileField(upload_to=post_video, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author.user.username}-post"


class Comment(models.Model):
    author = models.ForeignKey('users.profile', on_delete=models.SET_NULL, related_name='comment_author', blank=True,
                               null=True)
    post = models.ForeignKey('post.post', on_delete=models.CASCADE, related_name='comment_post')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author.user.username}-Comment"
