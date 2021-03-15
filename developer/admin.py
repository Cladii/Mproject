from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin

from .forms import DeveloperForm, DeveloperChangeForm
from .models import Developer
from task.models import Task
# Register your models here.

class TaskInline(admin.TabularInline):
    model = Task
    extra = 1

#class DeveloperAdmin(admin.ModelAdmin):
class DeveloperAdmin(UserAdmin):
    add_form = DeveloperForm
    form = DeveloperChangeForm
    fieldsets = UserAdmin.fieldsets + (('Team', {'fields': ['team',]}),)
    model = get_user_model()
    list_display = ('first_name', 'last_name', 'username', 'is_free')
    inlines = [TaskInline]

admin.site.register(Developer, DeveloperAdmin)