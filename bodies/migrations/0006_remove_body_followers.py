# Generated by Django 2.0.2 on 2018-03-03 20:05

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("bodies", "0005_auto_20180304_0127"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="body",
            name="followers",
        ),
    ]
