# Generated by Django 3.2.16 on 2023-12-10 07:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("lostandfound", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="productfound",
            options={
                "ordering": ("-time_of_creation",),
                "verbose_name": "ProductFound",
                "verbose_name_plural": "ProductsFound",
            },
        ),
        migrations.AddField(
            model_name="productfound",
            name="product_image1",
            field=models.ImageField(blank=True, upload_to="laf_images/"),
        ),
        migrations.AddField(
            model_name="productfound",
            name="product_image2",
            field=models.ImageField(blank=True, upload_to="laf_images/"),
        ),
        migrations.AddField(
            model_name="productfound",
            name="product_image3",
            field=models.ImageField(blank=True, upload_to="laf_images/"),
        ),
        migrations.AlterField(
            model_name="productfound",
            name="claimed",
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
