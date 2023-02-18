# Generated by Django 4.1.7 on 2023-02-18 08:10

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0002_alter_club_president"),
    ]

    operations = [
        migrations.AddField(
            model_name="club",
            name="image",
            field=cloudinary.models.CloudinaryField(default="", max_length=255),
        ),
    ]
