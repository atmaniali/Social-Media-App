from rest_framework import serializers

from users.models import Profile
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.HyperlinkedRelatedField(queryset=Profile.objects.all(), many=False, view_name='profile-detail')
    class Meta:
        model = Post
        fields = ['url', 'id', 'author', 'like', 'like_count', 'content', 'video', 'image', 'created_at']
        read_only_fields = ['created_at']
