# Generated by Django 4.2.20 on 2025-03-11 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("glasses", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="eyewear",
            name="quantity",
            field=models.PositiveIntegerField(default=1),
        ),
    ]
