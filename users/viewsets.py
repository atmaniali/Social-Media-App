import json
from django.utils import timezone
from rest_framework import viewsets, status
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.response import Response
import logging
from rest_framework import mixins
from rest_framework.authentication import TokenAuthentication

from .models import Profile, Friend, ACCEPTED, REJECTED, PENDING
from .serializer import (UserSerializer,
                         ProfileSerializer,
                         FriendSerializer,
                         FriendListSerializer)
from .permission import (IsUserOrGetOrPostOnly,
                         IsUserProfileOrGetOrPostOnly,
                         CustomTokenAuthentication)

logger = logging.getLogger(__name__)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsUserOrGetOrPostOnly]


class ProfileViewSet(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsUserProfileOrGetOrPostOnly]

        # TODO: add action to show list friend accepted
        # TODO: add action to accept friend
        # TODO: add action to show list friend refused
        # TODO: add action to refuse friend
        # TODO: add action to show list of en attend friend
        # TODO: add action to show en attend friend
    # @action(detail=True, methods=['get'], name='Friend List')
    # def get_list_of_friend(self, request, pk=None):
    #     try:
    #         instance = self.get_object()
    #         friends = instance.user_sent_request.filter(status=ACCEPTED)
    #         serializer = ProfileSerializer(instance=friends, context={'request':request})
    #         return Response({'friends': serializer.data}, status=status.HTTP_200_OK)
    #     except Exception as err:
    #         return Response({'detail': err}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


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

    @action(detail=False, methods=['get'], name='All Freinds Request')
    def get_all_friend_requests(self, request):
        try:
            logger.debug("ACTION CALLED")
            profile = Profile.objects.get(user=request.user.id)
            friend = Friend.objects.filter(status=ACCEPTED, user=profile)
            serializer = self.get_serializer(friend, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as err:
            return Response({'detail': str(err)}, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['put'], detail=True, permission_classes=[CustomTokenAuthentication])
    def accept_friend(self, request, pk=None):
        logger.debug("ACTION CUSTOM WORKING")
        try:
            friend = Friend.objects.get(pk=pk)
            print(friend)
            stat = request.data['status']
            print("status0", stat)
            if friend.status == ACCEPTED:
                raise Exception('Friend is Already accepted')
            elif friend.status == REJECTED:
                raise Exception('Friend is already rejected')
            else:
                print("friend",friend)
                friend.status = ACCEPTED
                friend.accepted = timezone.now()
                friend.save()

            serializer = FriendSerializer(instance=friend, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as err:
            return Response({'detail': str(err)}, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['put'], detail=True, permission_classes=[CustomTokenAuthentication])
    def delete_friend(self, request, pk=None):
        try:
            friend = Friend.objects.get(pk=pk)
            stat = request.data['status']
            if friend.status == REJECTED:
                raise Exception('Friend is Already rejected')
            else:
                friend.status = stat
                friend.rejected = timezone.now()
                friend.save()

            serializer = FriendSerializer(instance=friend, context={'request': request})
            return Response(serializer.data, status= status.HTTP_200_OK)
        except Exception as err:
            return Response({'detail': str(err)}, status=status.HTTP_400_BAD_REQUEST)
