from rest_framework import viewsets
from django.contrib.auth.models import User

from .models import Profile
from .serializer import UserSerializer, ProfileSerializer
from .permission import IsUserOrGetOrPostOnly, IsUserProfileOrGetOrPostOnly


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsUserOrGetOrPostOnly]


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsUserProfileOrGetOrPostOnly]
