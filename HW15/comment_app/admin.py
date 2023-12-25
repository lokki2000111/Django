from django.contrib import admin

from comment_app.models import Comment


# Register your models here.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'text')
    ordering = ('-created_at', '-id')
    readonly_fields = ('created_at', )
