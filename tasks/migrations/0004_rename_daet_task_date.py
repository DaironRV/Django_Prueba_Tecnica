# Generated by Django 5.1 on 2024-09-01 01:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_task_daet'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='daet',
            new_name='date',
        ),
    ]
