from django.conf.urls import url
from cources import views


urlpatterns =[
    url(r'crs', views.get_cources),
    url(r'add', views.add_pair, name='add')
]