from rest_framework import serializers

from .models import Message, Group
from users.models import Profile


class GroupSerializer(serializers.ModelSerializer):
    online = serializers.HyperlinkedRelatedField(queryset=Profile.objects.all(), many=True, view_name='profile-detail')

    class Meta:
        models = Group
        fields = ['url', 'id', 'name', 'online']


class MessageSerializer(serializers.ModelSerializer):
    group = serializers.HyperlinkedRelatedField(queryset=Group.objects.all(), many=False, view_name='group-detail')
    user = serializers.HyperlinkedRelatedField(queryset=Profile.objects.all(), many=False, view_name='profile-detail')

    class Meta:
        models = Message
        fields = ['url', 'id', 'content', 'user', 'group', 'timestamp']
