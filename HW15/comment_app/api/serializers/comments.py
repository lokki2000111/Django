from rest_framework import serializers

from comment_app.models import Comment
from like_app.api.serializers.likes import CommentLikeResponseSerializer
from user_serailizer import UserSerializer


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['user']

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source='user'
    )


class LikeCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = ['post', 'user']
        read_only_fields = ['user']

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source='user'
    )

    comment_likes = CommentLikeResponseSerializer(source='comment_like', many=True)
    user_like = UserSerializer(source='user')
