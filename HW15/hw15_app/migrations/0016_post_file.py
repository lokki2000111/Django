# Generated by Django 4.2.8 on 2023-12-22 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('media_app', '0001_initial'),
        ('hw15_app', '0015_remove_post_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='file',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='media_app.media'),
        ),
    ]