from django.db import models


# Create your models here.
class Currencies(models.Model):
    class Meta():
        db_table = 'currencies'
        verbose_name = 'Currency pairs'
        verbose_name_plural = 'Currency pairs'
        ordering = ["first_currency_short"]

    first_currency_long = models.CharField('First currency', max_length=15)
    first_currency_short = models.CharField('First currency short', max_length=5)
    second_currency_long = models.CharField('Second currency', max_length=15)
    second_currency_short = models.CharField('Second currency short', max_length=5)
    cource = models.FloatField('Cource value',max_length=15)

    def __str__(self):
        return self.cource

