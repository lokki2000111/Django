from django.contrib.auth.models import User
from django.db import models

from comment_app.models import Comment
from hw15_app.models import Post


class PostLike(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='user_post_like')
    post = models.ForeignKey(Post, on_delete=models.PROTECT, related_name="post_like")


class CommentLike(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='user_comment_like')
    comment = models.ForeignKey(Comment, on_delete=models.PROTECT, related_name='comment_like')
