from django.contrib import admin
from .models import Team

# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    list_display = ("name", "description")

admin.site.register(Team, TeamAdmin)