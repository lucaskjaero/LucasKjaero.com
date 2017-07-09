from django.conf.urls import url

from . import views

__author__ = 'lucas'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^page/(?P<page_number>[0-9]+)/$', views.index, name='index_with_number'),
    url(r'^view/(?P<slug>[A-Za-z0-9-]+)/$', views.detail, name='detail'),
    url(r'^category/(?P<category>[A-Za-z0-9-]+)/$', views.view_category, name='view_category')
]