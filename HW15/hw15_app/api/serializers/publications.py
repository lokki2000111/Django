from rest_framework import serializers

from comment_app.api.serializers.comments import LikeCommentSerializer
from hw15_app.models import Post
from like_app.api.serializers.likes import PostLikeResponseSerializer
from media_app.api.serializers.media import MediaSerializer
from tags_app.api.serializers.tags import TagSerializer
from user_serailizer import UserSerializer


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ['is_public']
        read_only_fields = ('id', 'user', 'is_public')
        extra_kwargs = {
            'file': {
                'required': True,
                'write_only': True,
                'help_text': 'Id медиа файла'
            }
        }

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source='user'
    )
    # media = serializers.URLField(source='file.file.url', read_only=True)
    media = MediaSerializer(source='file', allow_null=False, read_only=True)
    tags = TagSerializer(many=True, read_only=True)


class LikePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ['is_public', 'user']
        read_only_fields = ('id', 'user', 'is_public')

    post_likes = PostLikeResponseSerializer(source='post_like', many=True)
    comment = LikeCommentSerializer(source='post_comment', many=True)
    user_post = UserSerializer(source='user')
