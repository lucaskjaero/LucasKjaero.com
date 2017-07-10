from django.conf.urls import url

from . import views

__author__ = 'lucas'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^tech/(?P<technology>[A-Za-z0-9-]+)/$', views.technology, name='technology'),
    url(r'^project/(?P<project>[A-Za-z]+)/$', views.project, name='project'),
    url(r'^category/(?P<category>[A-Za-z0-9-]+)/$', views.view_category, name='view_category')

]
