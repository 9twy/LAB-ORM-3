# Generated by Django 4.2.13 on 2024-07-27 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="expirment",
            field=models.DateField(blank=True, null=True),
        ),
    ]