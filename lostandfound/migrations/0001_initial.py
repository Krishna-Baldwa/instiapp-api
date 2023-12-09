# Generated by Django 3.2.16 on 2023-11-29 14:14

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("users", "0040_remove_userprofile_followed_communities"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProductFound",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("str_id", models.CharField(editable=False, max_length=58, null=True)),
                ("name", models.CharField(max_length=60)),
                ("description", models.TextField(blank=True, default="")),
                ("product_image", models.TextField(blank=True, null=True)),
                (
                    "category",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("electronics", "Electronics"),
                            ("stationery", "Stationery"),
                            ("Other", "Other"),
                        ],
                        max_length=60,
                        null=True,
                    ),
                ),
                ("found_at", models.CharField(blank=True, default="", max_length=60)),
                ("claimed", models.BooleanField(blank=True, default=True, null=True)),
                ("contact_details", models.CharField(max_length=300)),
                ("time_of_creation", models.DateTimeField(auto_now_add=True)),
                (
                    "claimed_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="claimed_products",
                        to="users.userprofile",
                    ),
                ),
            ],
            options={
                "verbose_name": "Product",
                "verbose_name_plural": "Products",
                "ordering": ("-time_of_creation",),
            },
        ),
        migrations.AddIndex(
            model_name="productfound",
            index=models.Index(
                fields=["time_of_creation"], name="lostandfoun_time_of_e282f9_idx"
            ),
        ),
    ]
