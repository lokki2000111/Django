from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from tags_app.api.serializers.tags import TagSerializer
from tags_app.models import Tag


class TagsViewSet(APIView):
    serializer_class = TagSerializer

    @staticmethod
    def get(request, format=None):
        tags = [tag.tag_label for tag in Tag.objects.all()]
        return Response(tags)

# serializer_class = TagSerializer
# queryset = Tag.objects.all()
