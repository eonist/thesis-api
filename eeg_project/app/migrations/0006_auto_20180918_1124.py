# Generated by Django 2.1 on 2018-09-18 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20180912_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeframe',
            name='label',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='timeframes', to='app.Label'),
        ),
    ]