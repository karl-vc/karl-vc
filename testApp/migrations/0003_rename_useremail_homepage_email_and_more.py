# Generated by Django 4.0.1 on 2022-01-14 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0002_rename_usermame_homepage_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepage',
            old_name='userEmail',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='userName',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='userPassword',
            new_name='password',
        ),
    ]
