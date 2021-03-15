from django.shortcuts import render, get_object_or_404 
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import DetailView, ListView 
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Task
from .forms import TaskForm 

class IndexView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'task.task_management'
    model = Task
    template_name = "task/index.html"
    context_object_name = 'tasks' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TaskForm
        return context
    
def create(request):
    form = TaskForm(request.POST)

    if form.is_valid():
        Task.objects.create(
            title=form.cleaned_data['title'],
            description=form.cleaned_data['description'],
            assignee=form.cleaned_data['assignee'],
            project=form.cleaned_data['project'],)

    return HttpResponseRedirect(reverse('task:index'))

def delete(request,task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return HttpResponseRedirect(reverse('task:index')) 