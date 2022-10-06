from django import forms
from django.forms import ModelForm
from .models import Task

class TaskForm(ModelForm):
    title = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Title', 'class':'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Description', 'class':'form-control'}))
    class Meta:
        model = Task
        fields = ['title', 'description']   