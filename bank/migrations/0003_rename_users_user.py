# Generated by Django 3.2.7 on 2021-09-11 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0002_remove_users_contact'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='User',
        ),
    ]
