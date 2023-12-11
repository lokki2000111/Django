from django.apps import AppConfig
from django.core.signals import request_finished


class Hw15AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'hw15_app'

    def ready(self):
        from .signals import profile_signal
        request_finished.connect(profile_signal.post_saveuser)

