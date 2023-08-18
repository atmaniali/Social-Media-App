from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Profile, Friend


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True
    )
    email = serializers.EmailField(help_text="email should end with @gmail.com or @outlook.com")

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password('password')
        user.save()
        return user

    def validate_email(self, value):
        """
        Check if email contain @gmail, @outlook.com
        """
        value_split = value.split('@')
        email = value_split[1]
        if email not in ['gmail.com', 'outlook.com']:
            raise serializers.ValidationError(f'mail should contain @gmail.com or @outlook.com')

        return value

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'email', 'password']
        read_only_fields = []


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.HyperlinkedRelatedField(queryset=User.objects.all(), many=False, view_name='user-detail')

    class Meta:
        model = Profile
        fields = ['url', 'id', 'user', 'image', 'bio']


class FriendSerializer(serializers.ModelSerializer):
    user = serializers.HyperlinkedRelatedField(queryset=Profile.objects.all(), many=False, view_name='profile-detail')
    friend = serializers.HyperlinkedRelatedField(queryset=Profile.objects.all(), many=False, view_name='profile-detail')
    def create(self, validated_data):
        user = validated_data['user']
        friend = validated_data['friend']
        friend_ds = Friend.objects.get(user=friend, friend=user)
        if user == friend:
            raise serializers.ValidationError({"detail": "You can't send request to your self"})
        if friend_ds:
            raise serializers.ValidationError({'detail': f"You can't send request to be friend with {friend.user.username} you already friend with it."})
        return Friend.objects.create(**validated_data)

    class Meta:
        model = Friend
        fields = ['url', 'id', 'user', 'friend', 'status', 'created', 'rejected', 'accepted']
        read_only_fields = ['created', 'rejected', 'accepted']


class FriendListSerializer(serializers.ModelSerializer):
    # DONE: reformat user and friend fields to show link
    user = serializers.HyperlinkedRelatedField(queryset=Profile.objects.all(), many=True, view_name='prfile-detail')
    friend = serializers.HyperlinkedRelatedField(queryset=Profile.objects.all(), many=True, view_name='prfile-detail')

    class Meta:
        model = Friend
        fields = ['url', 'id', 'user', 'friend', 'status']
