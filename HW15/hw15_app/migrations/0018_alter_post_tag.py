# Generated by Django 4.2.8 on 2023-12-25 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags_app', '0001_initial'),
        ('hw15_app', '0017_remove_postimage_images_remove_postimage_post_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(related_name='post_tags', to='tags_app.tag'),
        ),
    ]
