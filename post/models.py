import uuid

from django.db import models


# Create your models here.


class Post(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4())
    author = models.OneToOneField('users.profile', on_delete=models.CASCADE)
    like = models.ForeignKey('users.profile', on_delete=models.SET_NULL, blank=True, null=True, related_name='post_like')
    content = models.TextField()
    image = models.ImageField(upload_to=f'posts/{id}/images/', blank=True, null=True)
    video = models.FileField(upload_to=f'post/{id}/videos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author.user.username}-post"


class Comment(models.Model):
    author = models.ForeignKey('users.profile', on_delete=models.SET_NULL, related_name='comment_author', blank=True, null=True)
    post = models.ForeignKey('post.post', on_delete=models.CASCADE, related_name='comment_post')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author.user.username}-Comment"



