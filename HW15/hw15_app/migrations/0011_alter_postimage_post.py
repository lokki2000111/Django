# Generated by Django 4.2.7 on 2023-12-05 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hw15_app', '0010_image_remove_post_post_image_postimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postimage',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_images', to='hw15_app.post'),
        ),
    ]
