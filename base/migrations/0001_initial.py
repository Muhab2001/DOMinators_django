# Generated by Django 4.1.7 on 2023-02-17 14:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="UserProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="user",
                    ),
                ),
            ],
            options={
                "verbose_name": "user profile",
                "verbose_name_plural": "user profiles",
            },
        ),
        migrations.CreateModel(
            name="Club",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, verbose_name="name")),
                ("logo", models.URLField(blank=True, verbose_name="logo")),
                (
                    "header_image",
                    models.URLField(blank=True, verbose_name="header image"),
                ),
                ("description", models.TextField(verbose_name="description")),
                ("theme", models.CharField(max_length=10, verbose_name="theme")),
                (
                    "twitter_link",
                    models.URLField(blank=True, verbose_name="twitter link"),
                ),
                (
                    "president",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="president",
                    ),
                ),
            ],
            options={
                "verbose_name": "club",
                "verbose_name_plural": "clubs",
            },
        ),
    ]
