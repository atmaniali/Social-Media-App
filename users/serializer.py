from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Profile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'email', 'password']


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model= Profile
        fields = ['url', 'id', 'user', 'image', 'bio']
