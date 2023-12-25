from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet

from like_app.api.serializers.likes import PostLikeResponseSerializer, CommentLikeResponseSerializer, \
    PostLikeRequestSerializer, CommentLikeRequestSerializer
from like_app.models import PostLike, CommentLike


class PostLikeViewSet(GenericViewSet, ListModelMixin, CreateModelMixin, RetrieveModelMixin):
    serializer_class = PostLikeRequestSerializer
    queryset = PostLike.objects.all()


class CommentLikeViewSet(GenericViewSet, ListModelMixin, CreateModelMixin, RetrieveModelMixin):
    serializer_class = CommentLikeRequestSerializer
    queryset = CommentLike.objects.all()
