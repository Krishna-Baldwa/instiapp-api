# Generated by Django 2.2.3 on 2019-07-20 12:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("achievements", "0006_auto_20190720_0355"),
    ]

    operations = [
        migrations.AddField(
            model_name="offeredachievement",
            name="generic",
            field=models.CharField(default="generic", max_length=20),
        ),
    ]
