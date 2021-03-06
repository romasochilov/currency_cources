# Generated by Django 2.0.1 on 2018-01-10 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cources', '0003_curencies_cource'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currencies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_currency_long', models.CharField(max_length=15, verbose_name='First currency')),
                ('first_currency_short', models.CharField(max_length=5, verbose_name='First currency short')),
                ('second_currency_long', models.CharField(max_length=15, verbose_name='Second currency')),
                ('second_currency_short', models.CharField(max_length=5, verbose_name='Second currency short')),
                ('cource', models.FloatField(max_length=15, verbose_name='Cource value')),
            ],
            options={
                'verbose_name': 'Currency pairs',
                'verbose_name_plural': 'Currency pairs',
                'db_table': 'currencies',
                'ordering': ['first_currency_short'],
            },
        ),
        migrations.DeleteModel(
            name='Curencies',
        ),
    ]
