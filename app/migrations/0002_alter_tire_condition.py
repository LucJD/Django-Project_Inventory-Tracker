# Generated by Django 4.1.5 on 2023-03-27 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tire",
            name="condition",
            field=models.IntegerField(
                choices=[(1, "Heavily Used"), (2, "Used"), (3, "Good"), (4, "New")],
                null=True,
            ),
        ),
    ]