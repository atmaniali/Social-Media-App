from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['url', 'id', 'author', 'like', 'content', 'video', 'image', 'created_at']
        read_only_fields = ['created_at']
