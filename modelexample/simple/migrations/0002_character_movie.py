# Generated by Django 4.1.5 on 2023-01-03 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("simple", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Character",
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
                ("name", models.CharField(max_length=50, verbose_name="Name")),
            ],
        ),
        migrations.CreateModel(
            name="Movie",
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
                ("name", models.CharField(max_length=50, verbose_name="Name")),
                (
                    "characters",
                    models.ManyToManyField(
                        to="simple.character", verbose_name="Characters"
                    ),
                ),
            ],
        ),
    ]
