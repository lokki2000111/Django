from rest_framework import routers

from comment_app.api.views.comments import CommentViewSet

api_router = routers.DefaultRouter()
api_router.register('comment', CommentViewSet)
