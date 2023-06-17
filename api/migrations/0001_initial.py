# Generated by Django 4.2.1 on 2023-06-17 17:03

import cloudinary.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='photos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('media', cloudinary.models.CloudinaryField(max_length=255)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
