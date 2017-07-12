"""RPi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from LucasKjaeroWebsite import views


urlpatterns = [
    url(r'^final/', views.final, name='final'),
    url(r'^resume/', views.resume, name='resume'),
    url(r'^gerenjianli/', views.gerenjianli, name='gerenjianli'),
    url(r'^gaojikouyu/', views.gaojikouyu, name="gaojikouyu"),
    url(r'^members/', views.members, name="members"),
    url(r'^blog/', include('blog.urls', namespace="blog")),
    url(r'^projects/', include('portfolio.urls', namespace="portfolio")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
]
