from rest_framework import serializers

from users.models import Profile
from .models import Post, Like, Comment


class PostSerializer(serializers.ModelSerializer):
    author = serializers.HyperlinkedRelatedField(queryset=Profile.objects.all(), many=False, view_name='profile-detail')

    class Meta:
        model = Post
        fields = ['url', 'id', 'author', 'like_count', 'content', 'video', 'image', 'created_at']
        read_only_fields = ['created_at']


class LikeSerializer(serializers.ModelSerializer):
    user = serializers.HyperlinkedRelatedField(queryset=Profile.objects.all(), many=False, view_name='profile-detail')
    post = serializers.HyperlinkedRelatedField(queryset=Post.objects.all(), many=False, view_name='post-detail')

    def create(self, validated_data):
        post_id = validated_data['post']
        user_id = validated_data['user']
        like = Like.objects.filter(post=post_id, user=user_id)
        print("like===", like)
        if like:
            raise serializers.ValidationError({'detail': 'You Have already Liked This Post'})
        return Like.objects.create(**validated_data)

    class Meta:
        model = Like
        fields = ['url', 'id', 'user', 'post']


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.HyperlinkedRelatedField(queryset=Profile.objects.all(), many=False, view_name='profile-detail')
    post = serializers.HyperlinkedRelatedField(queryset=Post.objects.all(), many=False, view_name='profile-detail')

    class Meta:
        model = Comment
        fields = ['url', 'id', 'author', 'post', 'content', 'created_at']
        read_only_fields = ['created_at']
