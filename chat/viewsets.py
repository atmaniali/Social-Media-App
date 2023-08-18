from rest_framework import viewsets

from .models import Group, Message
from .serializer import MessageSerializer, GroupSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class MessageSerializer(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
