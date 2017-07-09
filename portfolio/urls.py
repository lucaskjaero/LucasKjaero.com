from django.conf.urls import url

from . import views

__author__ = 'lucas'

urlpatterns = [
    url(r'^$', views.index, name='index'),
]