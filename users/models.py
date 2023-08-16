from django.db import models
from django.contrib.auth.models import User
import uuid


# Create your models here.

class Profile(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    image = models.FileField(upload_to=f'profiles/{id}/images/')

    def __str__(self):
        return f"{self.user.username}-profile"
