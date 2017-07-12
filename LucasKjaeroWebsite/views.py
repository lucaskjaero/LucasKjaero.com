from django.http import FileResponse
from django.shortcuts import render

from blog.models import Post

__author__ = 'lucas'

# TODO below a certain view size, text becomes unreadable


def index(request):
    latest_posts = Post.objects.filter(published=True).order_by('updated_at').reverse()[:2]

    context = {'latest_posts': latest_posts,
               }
    return render(request, 'index.html', context)


def final(request):
    context = {}
    return render(request, 'final.html', context)

def gaojikouyu(request):
    context = {}
    return render(request, 'gaojikouyu.html', context)

def members(request):
    context = {}
    return render(request, 'members.html', context)

def resume(request):
    return FileResponse(open('staticfiles/lucas-kjaero-resume.pdf', 'rb'), content_type='application/pdf')

def gerenjianli(request):
    return FileResponse(open('staticfiles/lucas-kjaero-gerenjianli.pdf', 'rb'), content_type='application/pdf')
