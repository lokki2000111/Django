from django.contrib import admin

from tags_app.models import Tag


# Register your models here.

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    model = Tag
