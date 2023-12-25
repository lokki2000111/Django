import re

from django.db.models.signals import post_save
from django.dispatch import receiver

from hw15_app.models import Post
from tags_app.models import Tag


@receiver(post_save, sender=Post)
def create_tag(sender, instance, created, *args, **kwargs):
    for tag_name in re.findall(r'#(\w+)', instance.text):
        tag, is_created = Tag.objects.get_or_create(tag_label=tag_name.lower())
        tag.post_tags.add(instance)
