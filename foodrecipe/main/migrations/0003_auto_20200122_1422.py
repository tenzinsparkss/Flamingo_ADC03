# Generated by Django 3.0.1 on 2020-01-22 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_users'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='User',
        ),
    ]
