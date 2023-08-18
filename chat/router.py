from rest_framework import routers

from .viewsets import GroupSerializer, MessageSerializer


router = routers.DefaultRouter()

router.register(r'groups', GroupSerializer)
router.register(r'messages', MessageSerializer)