# Generated by Django 2.0.1 on 2018-01-09 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cources', '0002_auto_20180109_1938'),
    ]

    operations = [
        migrations.AddField(
            model_name='curencies',
            name='cource',
            field=models.FloatField(default=0.0, max_length=15, verbose_name='Cource value'),
            preserve_default=False,
        ),
    ]
