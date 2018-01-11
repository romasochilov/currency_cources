from cources.models import Currencies
from django.forms import ModelForm

class CurrencyForm(ModelForm):
    class Meta:
        model = Currencies
        fields = ['first_currency_long',
                  'second_currency_long',
                  'first_currency_short',
                  'second_currency_short'
                  ]
