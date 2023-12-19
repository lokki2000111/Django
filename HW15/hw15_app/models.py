from django.contrib.auth.models import AbstractUser, User
from django.core.validators import RegexValidator
from django.db import models

from tags_app.models import Tag


class Image(models.Model):
    image = models.ImageField(blank=True, null=True)


class PostImage(models.Model):
    images = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='images')
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name='post_images')


class Info(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=256, unique=False, blank=False, null=False)
    last_name = models.CharField(max_length=256, unique=False, blank=False, null=False)
    about_me = models.TextField(blank=False, null=False, default='')
    is_public = models.BooleanField(default=True)


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=256, unique=False, blank=False, null=False)
    text = models.TextField(blank=False, null=False)
    is_public = models.BooleanField(default=True)
    tag = models.ManyToManyField(Tag, null=True, blank=True, related_name='post_tags')


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='media/', blank=True, null=True)
    phone = models.CharField(validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$')], max_length=17, blank=True,
                             null=True)
    about = models.TextField(max_length=4096)
    social_link = models.URLField(blank=True, null=True)
