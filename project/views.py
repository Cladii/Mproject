from django.shortcuts import render, get_object_or_404 
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import DetailView, ListView 
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Project
from .forms import ProjectForm 

class IndexView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'project.project_management'
    model = Project
    template_name = "project/index.html"
    context_object_name = 'projects' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ProjectForm
        return context
    
def create(request):
    form = ProjectForm(request.POST)

    if form.is_valid():
        Project.objects.create(
            name=form.cleaned_data['name'],
            resume=form.cleaned_data['resume'],)

    return HttpResponseRedirect(reverse('project:index'))
