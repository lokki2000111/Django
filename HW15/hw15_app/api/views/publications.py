from rest_framework import filters
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from hw15_app.api.serializers.publications import PostSerializer
from hw15_app.models import Post


class PostsView(GenericViewSet, ListModelMixin, CreateModelMixin):
    serializer_class = PostSerializer
    queryset = Post.objects.filter(is_public=True)
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['created_at']


class PostForTagView(APIView):
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        tag = kwargs.get('tag')
        queryset = Post.objects.filter(tag__tag_label=tag).all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)
