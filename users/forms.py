from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    #add additional fields needed
    email = forms.EmailField()

    class Meta: #give a nested namespace for configurations and keeps it in same place.
        model = User
        fields = ['username', 'email']
