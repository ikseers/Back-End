# Generated by Django 4.2.6 on 2024-02-16 20:59
import django.core.validators
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0005_remove_product_image_product_code_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productrating",
            name="comment",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="productrating",
            name="rating",
            field=models.IntegerField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(5),
                ],
            ),
        ),
    ]