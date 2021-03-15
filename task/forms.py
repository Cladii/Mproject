from django import forms
from .models import Task

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['title', 'description', 'assignee','project']

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['assignee'].required = False
        self.fields['project'].required = False
