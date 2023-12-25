from rest_framework import serializers

from user_serailizer import UserSerializer
from like_app.models import PostLike, CommentLike


class PostLikeResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLike
        exclude = ['post', 'user']
        read_only_fields = ['user']

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source='user'
    )

    user_post = UserSerializer(source='user')


class PostLikeRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLike
        fields = '__all__'
        read_only_fields = ['user']

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source='user'
    )


class CommentLikeResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentLike
        exclude = ['comment', 'user']
        read_only_fields = ['user']

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source='user'
    )

    user_comment = UserSerializer(source='user')


class CommentLikeRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentLike
        fields = '__all__'
        read_only_fields = ['user']

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source='user'
    )
