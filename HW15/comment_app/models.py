from django.contrib.auth.models import User
from django.db import models


from hw15_app.models import Post


class Comment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=1024)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_user')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comment')

