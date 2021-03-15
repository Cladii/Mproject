from django.db import models
from developer.models import Developer
from project.models import Project

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    assignee = models.ForeignKey(Developer, related_name="tasks", on_delete = models.SET_NULL, null=True, verbose_name="assignee")
    project = models.ForeignKey(Project,related_name="tasksproject", on_delete = models.CASCADE, null=True, verbose_name="project")

    class Meta: 
        permissions = [
            ('task_management', 'Can create, assign and delete task'),
        ]

    def __str__(self):
        return f"{self.title} ({self.description})"    
