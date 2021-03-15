from django.db import models

# Create your models here.

class Team(models.Model):
    name = models.CharField("name", max_length=200)
    description = models.TextField("description") 

    class Meta:
        permissions = [
            ('team_management', 'Can create, assign and delete project'),
        ]