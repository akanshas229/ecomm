# Generated by Django 3.2.5 on 2021-07-15 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='last_name',
        ),
    ]
