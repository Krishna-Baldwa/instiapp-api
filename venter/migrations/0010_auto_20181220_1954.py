# Generated by Django 2.1.4 on 2018-12-20 14:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("venter", "0009_auto_20181129_2144"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="complaints",
            name="email_status",
        ),
        migrations.AddField(
            model_name="complaints",
            name="email_sent_to",
            field=models.TextField(blank=True),
        ),
    ]
