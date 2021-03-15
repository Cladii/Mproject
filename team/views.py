from django.shortcuts import render, get_object_or_404 
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import DetailView, ListView 
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Team
from .forms import TeamForm

# Create your views here.
class IndexView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'team.team_management'
    model = Team
    template_name = "team/index.html"
    context_object_name = 'teams' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TeamForm
        return context
    
def create(request):
    form = TeamForm(request.POST)

    if form.is_valid():
        Team.objects.create(
            name=form.cleaned_data['name'],
            description=form.cleaned_data['description'],)

    return HttpResponseRedirect(reverse('team:index'))

