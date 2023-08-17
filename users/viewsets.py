import json

from rest_framework import viewsets, status
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.response import Response
import logging


from .models import Profile, Friend, ACCEPTED
from .serializer import (UserSerializer,
                         ProfileSerializer,
                         FriendSerializer,
                         FriendListSerializer)
from .permission import (IsUserOrGetOrPostOnly,
                         IsUserProfileOrGetOrPostOnly)


logger = logging.getLogger(__name__)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsUserOrGetOrPostOnly]


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsUserProfileOrGetOrPostOnly]

    @action(detail=True, methods=['get'], name='Friend List')
    def get_list_of_friend(self, request, pk=None):
        # TODO: add action to show list friend accepted
        # TODO: add action to accept friend
        # TODO: add action to show list friend refused
        # TODO: add action to refuse friend
        # TODO: add action to show list of en attend friend
        # TODO: add action to show en attend friend
        try:
            instance = self.get_object()
            friends = Friend.objects.filter(user=instance, status=ACCEPTED)
            # serializer = FriendListSerializer(friends, many=True)
            json_data = json.dumps(list(friends))
            return Response({'friends': 'json_data'}, status=status.HTTP_200_OK)
        except Exception as err:
            return Response({'detail': err}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class FriendViewSet(viewsets.ModelViewSet):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer

    def get_queryset(self):
        """
        Override queryset to just show friend bellow to user
        """
        queryset = super(FriendViewSet, self).get_queryset()
        if not self.request.user.is_anonymous:
            profile = Profile.objects.get(user=self.request.user)
            user_friend = queryset.filter(user=profile)
            return user_friend

    @action(detail=True, name='All Freind Request')
    def get_all_friend_requests(self, request):
        friend_requests = Friend.objects.filter(
            user_id=request.user.id,
            status='pending'
        )
        return Response(friend_requests.to_json(), status=status.HTTP_200_OK)