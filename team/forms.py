from django import forms
from .models import Team

class TeamForm(forms.ModelForm):

    class Meta:
        model = Team
        fields = ['name', 'description']

    def __init__(self, *args, **kwargs):
        super(TeamForm, self).__init__(*args, **kwargs)
