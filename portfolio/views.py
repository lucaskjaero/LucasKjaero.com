from django.shortcuts import render, get_object_or_404

from .models import Category, Project, Technology

# Create your views here.
def index(request):
    projects = Project.objects.order_by('difficulty').reverse()
    return render(request, 'portfolio/index.html', {'projects': projects})


def technology(request, technology):
    selected_technology = get_object_or_404(Technology, name=technology)
    projects = Project.objects.filter(technologies=selected_technology)
    return render(request, 'portfolio/view_technology.html', {'projects': projects, 'technology': selected_technology})


def project(request, project):
    project = get_object_or_404(Project, name=project)
    return render(request, 'portfolio/view_project.html', {'project': project})


def view_category(request, category):
    selected_category = get_object_or_404(Category, name=category)
    projects = Project.objects.filter(category=selected_category)
    return render(request, 'portfolio/view_category.html', {'projects': projects, 'category': selected_category})
