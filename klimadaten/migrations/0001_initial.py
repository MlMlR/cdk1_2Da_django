# Generated by Django 5.0.6 on 2024-06-23 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="City",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255)),
                ("country", models.CharField(max_length=255)),
                ("iso2", models.CharField(max_length=2)),
                ("iso3", models.CharField(max_length=3)),
                ("lat", models.DecimalField(decimal_places=6, max_digits=9)),
                ("lon", models.DecimalField(decimal_places=6, max_digits=9)),
            ],
        ),
        migrations.CreateModel(
            name="Station",
            fields=[
                ("staid", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255)),
                ("country", models.CharField(max_length=255)),
                ("lat", models.DecimalField(decimal_places=6, max_digits=9)),
                ("lon", models.DecimalField(decimal_places=6, max_digits=9)),
                ("elevation", models.DecimalField(decimal_places=2, max_digits=9)),
            ],
        ),
    ]
