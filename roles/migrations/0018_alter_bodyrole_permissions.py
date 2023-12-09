# Generated by Django 3.2.13 on 2022-08-27 17:33

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):
    dependencies = [
        ("roles", "0017_alter_bodyrole_permissions"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bodyrole",
            name="permissions",
            field=multiselectfield.db.fields.MultiSelectField(
                choices=[
                    ("AddE", "Add Event"),
                    ("UpdE", "Update Event"),
                    ("DelE", "Delete Event"),
                    ("UpdB", "Update Body"),
                    ("Role", "Modify Roles"),
                    ("VerA", "Verify Achievements"),
                    ("AppP", "Approve Post"),
                    ("ModC", "Moderate Comment"),
                ],
                max_length=39,
            ),
        ),
    ]
