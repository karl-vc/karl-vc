# Generated by Django 4.0.1 on 2022-01-14 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('userMame', models.CharField(default='', max_length=200)),
                ('userEmail', models.CharField(default='', max_length=200, primary_key=True, serialize=False)),
                ('userPassword', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
