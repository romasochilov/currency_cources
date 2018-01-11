from django.shortcuts import render
from cources.utils.watch_cource import  CryptonatorCource
from cources.models import Currencies
from cources.forms import CurrencyForm



# Create your views here.
def get_cources(request):
    pair = Currencies.objects.all()
    cur = Currencies.objects.get(pk=1)
    form = CurrencyForm(instance=cur)
    for p in pair.all():
        _c = CryptonatorCource(p.first_currency_short,
                               p.second_currency_short
                               )
        try:
            p.cource = float(_c.cource())
        except Exception as ex:
            error = ex
        Currencies.save(p)
    return render(request,
                  'cources.html',
                  {'pairs': pair},
                  {'form': form},
                  )


def add_pair(request):
    if request.method == 'POST':
        form = CurrencyForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.cource = 0.0
            post.save()
        #Currencies.objects.create()
    else:
        form = CurrencyForm()
    return render(request, 'add.html', {'form': form})
