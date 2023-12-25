from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet

from comment_app.api.serializers.comments import CommentSerializer
from comment_app.models import Comment


class CommentViewSet(GenericViewSet, ListModelMixin, CreateModelMixin, RetrieveModelMixin):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
