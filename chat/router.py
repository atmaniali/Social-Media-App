from rest_framework import routers

from .viewsets import GroupViewSet, MessageViewSet


router = routers.DefaultRouter()

router.register(r'groups', GroupViewSet)
router.register(r'messages', MessageViewSet)