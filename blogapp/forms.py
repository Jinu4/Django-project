from .models import Blogs
from django import forms


class ModelForm(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = ['title', 'desc', 'image']
