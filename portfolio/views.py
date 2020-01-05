from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

import os

import sendgrid
from sendgrid.helpers.mail import Content, Email, Mail

from .forms import NameForm
from .models import Category, Project, Technology

import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


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


def request_source(request, project):
    if request.method == 'POST':
        form = NameForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            agreement = form.cleaned_data['agreement']

            to_email = Email('lucas@lucaskjaero.com')
            from_email = Email('django@lucaskjaero.com')

            subject = "Source for %s has been requested" % project
            message = "Source for %s has been requested\nName: %s\nEmail: %s" % (project, name, email)
            content = Content("text/plain", message)

            sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
            mail = Mail(from_email, subject, to_email, content)

            if agreement:
                sg.client.mail.send.post(request_body=mail.get())
                messages.success(request, 'Source has been requested.')
            else:
                messages.error(request, 'You need to agree to the terms.')

            return HttpResponseRedirect(reverse("portfolio:project", args=[project]))
        else:
            messages.error(request, 'Submitted form was invalid.')

    else:
        form = NameForm()

    return render(request, 'portfolio/request_source.html', {'form': form, 'project': project})
