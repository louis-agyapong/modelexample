# Generated by Django 4.1.5 on 2023-01-04 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("school", "0001_initial"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Course",
        ),
        migrations.DeleteModel(
            name="Student",
        ),
    ]
