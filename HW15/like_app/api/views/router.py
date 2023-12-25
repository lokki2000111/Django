from rest_framework import routers

from like_app.api.views.likes import PostLikeViewSet, CommentLikeViewSet

api_router = routers.DefaultRouter()
api_router.register('post_like', PostLikeViewSet)
api_router.register('comment_like', CommentLikeViewSet)

