from django.db import models
from django.forms import ModelForm

class Project(models.Model):
    name = models.CharField(max_length=100)

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name']
