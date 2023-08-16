from rest_framework import routers

from .viewsets import ProfileViewSet, UserViewSet, FriendViewSet

router = routers.DefaultRouter()

router.register(r'user', UserViewSet)
router.register(r'profile', ProfileViewSet)
router.register('friend', FriendViewSet)