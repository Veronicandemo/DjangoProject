# Generated by Django 4.2.1 on 2023-06-04 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='position',
            new_name='role',
        ),
    ]
