# Generated by Django 4.2.1 on 2023-09-16 08:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('photosapp', '0007_remove_photos_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='photos',
            name='user',
            field=models.ForeignKey(default=6, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
