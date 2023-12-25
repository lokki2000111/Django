from rest_framework import filters
from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin, UpdateModelMixin, \
    RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from hw15_app.api.serializers.publications import PostSerializer, PostLikeResponseSerializer, LikePostSerializer
from hw15_app.models import Post


class PostsViewSet(GenericViewSet, ListModelMixin, CreateModelMixin, DestroyModelMixin, UpdateModelMixin,
                   RetrieveModelMixin):
    serializer_class = PostSerializer
    queryset = Post.objects.filter(is_public=True)
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['created_at']


class PostForTagView(APIView):

    def get(self, request, *args, **kwargs):
        tag = kwargs.get('tag')
        queryset = Post.objects.filter(tag__tag_label=tag).all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)


class PostLikeView(APIView):
    serializer_class = LikePostSerializer

    def get(self, request, *args, **kwargs):
        post_id = kwargs.get('id')
        queryset = Post.objects.filter(pk=post_id)
        serializer = LikePostSerializer(queryset, many=True)
        return Response(serializer.data)
