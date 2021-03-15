from django.urls import path
from . import views
from .views import IndexView

app_name = 'project'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('create', views.create, name="create"),
    #path('<int:task_id>/delete', views.delete, name='delete'),
]