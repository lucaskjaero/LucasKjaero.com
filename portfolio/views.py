from django.shortcuts import render, get_object_or_404

from .models import Category, Project, Technology

# Create your views here.
def index(request):
    categories = Category.objects.order_by('name')
    technologies = Technology.objects.order_by('name')
    projects = Project.objects.order_by('difficulty').reverse()
    return render(request, 'portfolio/index.html', {'categories': categories, 'projects': projects, 'technologies': technologies})


def technology(request, technology):
    selected_technology = get_object_or_404(Technology, slug=technology)
    projects = Project.objects.filter(technologies=selected_technology).order_by('difficulty').reverse()
    return render(request, 'portfolio/view_technology.html', {'projects': projects, 'technology': selected_technology})


def project(request, project):
    project = get_object_or_404(Project, slug=project)
    return render(request, 'portfolio/view_project.html', {'project': project})


def view_category(request, category):
    selected_category = get_object_or_404(Category, slug=category)
    projects = Project.objects.filter(categories=selected_category).order_by('difficulty').reverse()
    return render(request, 'portfolio/view_category.html', {'projects': projects, 'category': selected_category})
