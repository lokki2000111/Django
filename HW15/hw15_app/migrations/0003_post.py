# Generated by Django 4.2.7 on 2023-11-28 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hw15_app', '0002_info_about_me'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=256)),
                ('text', models.TextField()),
                ('is_public', models.BooleanField(default=True)),
            ],
        ),
    ]