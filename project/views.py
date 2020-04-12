from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect

from .models import Project, ProjectForm

def index(request):
    projects_list = Project.objects.all()
    context = {
        'projects_list': projects_list,
    }
    template = loader.get_template('project/index.html')
    return HttpResponse(template.render(context, request))

def save(request):
    project = ProjectForm(request.POST)
    project.save()
    return HttpResponseRedirect('/')
    
