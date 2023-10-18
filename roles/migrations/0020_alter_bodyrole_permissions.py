# Generated by Django 3.2.16 on 2023-10-14 17:40

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('roles', '0019_alter_bodyrole_permissions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bodyrole',
            name='permissions',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('AddE', 'Add Event'), ('UpdE', 'Update Event'), ('DelE', 'Delete Event'), ('UpdB', 'Update Body'), ('Role', 'Modify Roles'), ('VerA', 'Verify Achievements'), ('AppP', 'Moderate Post'), ('ModC', 'Moderate Comment'), ('GCAdmin', 'GC Admin')], max_length=47),
        ),
    ]
