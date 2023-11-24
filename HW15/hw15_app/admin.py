from django.contrib import admin

from hw15_app.models import Info


# Register your models here.
@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'first_name', 'last_name')
    ordering = ('id', 'created_at')
    readonly_fields = ('created_at',)
