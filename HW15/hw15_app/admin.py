from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as UserAdminBase
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

from hw15_app.models import Info, Post, Profile


# Register your models here.
@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'first_name', 'last_name')
    ordering = ('id', 'created_at')
    readonly_fields = ('created_at',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'title', 'text')


class PostInline(admin.StackedInline):
    model = Post
    list_display = ['created_at',
                    'title',
                    'text',
                    'is_public',
                    'profile',
                    'post_image_preview',
                    ]

    readonly_fields = ['post_image_preview']

    def post_image_preview(self, obj):
        # image = obj.post_image

        if obj.post_image:
            return mark_safe(
                f'<a href="{obj.post_image.url}">'
                f'<img src="{obj.post_image.url}" width=100px height=100px>'
                f'</a>'
            )

    post_image_preview.short_description = 'фотки поста'


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'avatar_preview')

    inlines = (
        PostInline,
    )

    @staticmethod
    def avatar_preview(obj):
        if obj.avatar:
            return mark_safe(
                f'<a href="{obj.avatar.url}">'
                f'<img src="{obj.avatar.url}" width=100px height=100px>'
                f'</a>'
            )


admin.site.unregister(User)


class ProfileInline(admin.StackedInline):
    model = Profile


@admin.register(User)
class UserAdmin(UserAdminBase):
    inlines = (
        ProfileInline,
    )
