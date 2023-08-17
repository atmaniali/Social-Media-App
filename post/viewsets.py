from rest_framework import viewsets
from rest_framework.decorators import action

from .models import Post
from .serializer import PostSerializer
from .permission import IsOutherOnlyOrGetOrPost


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [IsOutherOnlyOrGetOrPost]
    serializer_class = PostSerializer

    @action(methods=['get'], detail=True)
    def list_likes(self):
        pass

