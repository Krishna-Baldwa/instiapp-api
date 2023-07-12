# Generated by Django 3.2.16 on 2023-07-07 14:40

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0028_auto_20221003_2130'),
        ('roles', '0019_alter_bodyrole_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommunityRole',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('time_of_creation', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=50)),
                ('inheritable', models.BooleanField(default=False)),
                ('permissions', multiselectfield.db.fields.MultiSelectField(choices=[('AddE', 'Add Event'), ('UpdE', 'Update Event'), ('DelE', 'Delete Event'), ('UpdB', 'Update Body'), ('Role', 'Modify Roles'), ('VerA', 'Verify Achievements'), ('AppP', 'Moderate Post'), ('ModC', 'Moderate Comment')], max_length=39)),
                ('priority', models.IntegerField(default=0)),
                ('official_post', models.BooleanField(default=True)),
                ('permanent', models.BooleanField(default=False)),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roles', to='community.community')),
            ],
            options={
                'verbose_name': 'Community Role',
                'verbose_name_plural': 'Community Roles',
                'ordering': ('community__name', 'priority'),
            },
        ),
    ]
