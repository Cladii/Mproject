from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Developer
from .forms import DeveloperForm
from .forms import ShortDeveloperForm
from task.forms import TaskForm

def index(request):
    #return HttpResponse("Hello, world. You're at the developers index.")
    context = {
        'developers' : Developer.objects.all(),
        'form': DeveloperForm,
    }
    return render(request, 'developer/index.html', context)

class DevDetailVue(LoginRequiredMixin, DetailView):
    model = Developer
    template_name = 'developer/detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        form = TaskForm(initial={'assignee' : get_object_or_404(Developer, pk=self.kwargs['pk'])})
        form.fields['assignee'].disabled = True
        context["form"] = form
        return context
    
#def detail(request, developer_id):
#    developer = Developer.objects.get(pk=developer_id)
#    developer = get_object_or_404(Developer, pk=developer_id)
#    return render(request, 'developer/detail.html', {'developer': developer})

class IndexView(LoginRequiredMixin, ListView):
    model = Developer
    template_name = "developer/index.html"
    context_object_name = 'developers'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        #context['form'] = DeveloperForm
        context['form'] = ShortDeveloperForm
        return context

def create(request):
    form = ShortDeveloperForm(request.POST)
    if form.is_valid():
        Developer.objects.create(
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
            username=form.cleaned_data['username'],
            team=form.cleaned_data['team'],
        )
    #Developer.objects.create(
    #    first_name = request.POST['first_name'],
    #    last_name = request.POST['last_name']
    #)
    # Toujours renvoyer une HTTPResponseRedirect après avoir géré correctement
    # les données de la requête POST. Cela empêche les données d'être postée deux
    # fois si l'utilisateur clique sur le bouton précédent
    return HttpResponseRedirect(reverse('developer:index'))

def delete(request, id):
    Developer.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('developer:index'))