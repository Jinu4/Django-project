from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    profile_image = forms.FileField()
    description = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'email', 'description', 'password1', 'password2', 'profile_image']
