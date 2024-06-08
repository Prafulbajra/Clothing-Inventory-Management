# Generated by Django 5.0.6 on 2024-06-08 06:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cloth_inv", "0004_alter_cloth_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cloth",
            name="category",
            field=models.CharField(
                choices=[
                    ("SH", "Shirt"),
                    ("PT", "Pant"),
                    ("TS", "T-Shirt"),
                    ("ST", "Suit"),
                    ("IW", "Innerwear"),
                ],
                max_length=3,
            ),
        ),
        migrations.AlterField(
            model_name="cloth",
            name="size",
            field=models.CharField(
                choices=[
                    ("S", "S"),
                    ("M", "M"),
                    ("L", "L"),
                    ("XL", "XL"),
                    ("XXL", "XXL"),
                ],
                default="L",
                max_length=3,
            ),
        ),
    ]
