# Generated by Django 4.0.1 on 2022-01-24 05:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0009_worlddata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worlddata',
            name='city',
        ),
        migrations.RemoveField(
            model_name='worlddata',
            name='state',
        ),
    ]
