# Generated by Django 4.1.7 on 2023-02-17 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0001_initial"),
    ]

    operations = [
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
            ],
            options={
                "verbose_name": "club",
                "verbose_name_plural": "clubs",
            },
        ),
    ]
