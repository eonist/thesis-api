# Generated by Django 2.1 on 2018-09-12 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='real_data',
            field=models.BooleanField(default=False),
        ),
    ]
