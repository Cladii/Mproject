from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import Developer

class DeveloperForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'username', 'email')

class DeveloperChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'username', 'email', 'team')

class ShortDeveloperForm(forms.ModelForm):
    class Meta:
        model = Developer
        fields = ['first_name', 'last_name', 'username','team']

#class DeveloperForm(forms.ModelForm):
    #first_name = forms.CharField(label="First name", max_length=100)
    #last_name = forms.CharField(max_length=100)
    #class Meta:
    #   model = Developer
    #    fields = ['first_name' , 'last_name']