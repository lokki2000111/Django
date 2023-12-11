from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from hw15_app.models import Profile


@receiver(post_save, sender=User)
def post_saveuser(**kwargs):
    instance = kwargs.get('instance', None)
    created = kwargs.get('created', None)
    if instance:
        user = User.objects.get(pk=instance.id)

        if created:
            profile = Profile(user=user)
            profile.save()
