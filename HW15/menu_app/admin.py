from django.contrib import admin

from menu_app.models import Menu, MenuItem


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    model = Menu


@admin.register(MenuItem)
class MenuItemsAdmin(admin.ModelAdmin):
    model = MenuItem
