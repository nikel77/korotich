# Generated by Django 3.0.2 on 2020-02-01 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailer', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='read_marker',
            new_name='is_read',
        ),
    ]
