# Generated by Django 3.2.6 on 2021-11-19 19:25

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("users", "0037_auto_20201101_1943"),
    ]

    operations = [
        migrations.CreateModel(
            name="Query",
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
                ("question", models.TextField()),
                ("answer", models.TextField()),
                ("category", models.CharField(max_length=30)),
                ("sub_category", models.CharField(blank=True, max_length=30)),
                ("sub_sub_category", models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name="UnresolvedQuery",
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
                ("question", models.TextField()),
                ("category", models.CharField(blank=True, max_length=30)),
                ("resolved", models.BooleanField(default=False)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="Query",
                        to="users.userprofile",
                    ),
                ),
            ],
        ),
    ]
