from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField("name", max_length=200)
    resume = models.TextField("resume")

    class Meta: 
        permissions = [
            ('project_management', 'Can create, assign and delete project'),
        ]

    def __str__(self):
        return f"{self.name}"
