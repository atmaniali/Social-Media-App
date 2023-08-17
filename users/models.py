import os

from django.db import models
from django.contrib.auth.models import User
import uuid
from django.utils.deconstruct import deconstructible

# Create your models here.

PENDING = 'pending'
ACCEPTED = 'accepted'
REJECTED = 'rejected'
FRIEND_STATUS = (
    (PENDING, 'pending'),
    (ACCEPTED, 'accepted'),
    (REJECTED, 'rejected')
)


@deconstructible
class GeneratePathProfilePhoto(object):
    def __int__(self):
        pass

    def __call__(self, instance, filename):
        ext = filename.split(".")[-1]
        path = f"profile/{instance.user.id}/images/"
        name = f"post_image.{ext}"
        return os.path.join(path, name)


user_profile_path = GeneratePathProfilePhoto()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    image = models.FileField(upload_to=user_profile_path, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}-profile"


class Friend(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='user_sent_request')
    friend = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='user_accept_request')
    status = models.CharField(max_length=100, choices=FRIEND_STATUS, default=PENDING)
    created = models.DateTimeField(auto_now=True)
    accepted = models.DateTimeField(blank=True, null=True)
    rejected = models.DateTimeField(blank=True, null=True)

    def to_json(self):
        return {
            'id': self.id,
            'user': self.user,
            'friend': self.friend,
            'status': self.status
        }

    def __str__(self):
        return f"user: {self.user.user.username} sent request to {self.friend.user.username}"

    def to_dict(self):
        return {
            'user': self.user.username,
            'friend': self.friend.username,
            'status': self.status
        }
