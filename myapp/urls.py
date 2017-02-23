from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.store_list, name='store_list'),
    url(r'^store/(?P<pk>\d+)/$', views.store_detail, name='store_detail'),
    url(r'^store/new/$', views.store_new, name='store_new'),
]