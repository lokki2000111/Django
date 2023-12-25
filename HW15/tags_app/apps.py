from django.apps import AppConfig


class TagsAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tags_app'

    def ready(self):
        from hw15_app.signals import hashtag_signal
