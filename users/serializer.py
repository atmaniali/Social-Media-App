from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Profile


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        style={'input_type':'password'},
        write_only=True
    )
    email = serializers.EmailField()

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
        if email != 'gmail.com' or email != 'outlook.com':
            raise serializers.ValidationError(f'mail should contain @gmail.com or @outlook.com')

        return value

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'email', 'password']
        read_only_fields = []


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model= Profile
        fields = ['url', 'id', 'user', 'image', 'bio']
