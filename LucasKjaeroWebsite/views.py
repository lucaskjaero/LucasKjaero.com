from django.http import FileResponse
from django.shortcuts import render

from blog.models import Post
from portfolio.models import Project

__author__ = 'lucas'

# TODO below a certain view size, text becomes unreadable


def index(request):
    latest_posts = Post.objects.filter(published=True).order_by('updated_at').reverse()[:2]

    hardest_projects = Project.objects.filter(visible=True).order_by('difficulty').reverse()[:3]

    context = {'latest_posts': latest_posts,
               'projects': hardest_projects, }
    return render(request, 'index.html', context)


def resume(request):
    return FileResponse(open('LucasKjaeroWebsite/static/lucas-kjaero-resume.pdf', 'rb'), content_type='application/pdf')


def gerenjianli(request):
    return FileResponse(open('LucasKjaeroWebsite/static/lucas-kjaero-gerenjianli.pdf', 'rb'), content_type='application/pdf')
