# Generated by Django 4.1.7 on 2023-02-18 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0005_alter_club_header_image_alter_club_logo"),
    ]

    operations = [
        migrations.AddField(
            model_name="club",
            name="facebook_link",
            field=models.URLField(blank=True, default="", verbose_name="twitter link"),
        ),
        migrations.AddField(
            model_name="club",
            name="instagram_link",
            field=models.URLField(blank=True, default="", verbose_name="twitter link"),
        ),
        migrations.AlterField(
            model_name="club",
            name="twitter_link",
            field=models.URLField(blank=True, default="", verbose_name="twitter link"),
        ),
    ]
