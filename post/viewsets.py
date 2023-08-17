from rest_framework import viewsets
from rest_framework.decorators import action

from users.models import Profile
from .models import Post, Like, Comment
from .serializer import PostSerializer, LikeSerializer, CommentSerializer
from .permission import IsOutherOnlyOrGetOrPost


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [IsOutherOnlyOrGetOrPost]
    serializer_class = PostSerializer

    @action(methods=['get'], detail=True)
    def list_likes(self):
        pass


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    # permission_classes = [IsOutherOnlyOrGetOrPost]
    serializer_class = LikeSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    # permission_classes = [IsOutherOnlyOrGetOrPost]
    serializer_class = CommentSerializer

    def get_queryset(self):
        """
        Overid query to just show comment bellow to user
        """
        instance = super(CommentViewSet, self).get_queryset()
        if self.request.user.is_authenticated:
            profile = Profile.objects.get(user=self.request.user)
            comment = Comment.objects.filter(author=profile)
            return comment
