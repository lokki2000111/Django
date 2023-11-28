from django.db import models


# Create your models here.

class Info(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=256, unique=False, blank=False, null=False)
    last_name = models.CharField(max_length=256, unique=False, blank=False, null=False)
    about_me = models.TextField(blank=False, null=False, default='')
    is_public = models.BooleanField(default=True)


class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=256, unique=False, blank=False, null=False)
    text = models.TextField(blank=False, null=False)
    is_public = models.BooleanField(default=True)
