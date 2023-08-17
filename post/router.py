from rest_framework import routers

from .viewsets import PostViewSet, LikeViewSet, CommentViewSet

router = routers.DefaultRouter()


router.register(r'post', PostViewSet)
router.register(r'like', LikeViewSet)
router.register(r'comment', CommentViewSet)
