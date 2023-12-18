# Generated by Django 4.2.8 on 2023-12-12 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu_app', '0004_alter_menu_menu_label_alter_menuitem_menu'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='menuitem',
            unique_together={('menu', 'title')},
        ),
        migrations.AddIndex(
            model_name='menuitem',
            index=models.Index(fields=['menu'], name='menu_app_me_menu_id_a0f054_idx'),
        ),
        migrations.AddIndex(
            model_name='menuitem',
            index=models.Index(fields=['menu', 'url'], name='menu_app_me_menu_id_131b4b_idx'),
        ),
    ]
