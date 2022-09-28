from django import forms
from django.forms import ModelForm
from .models import Task

class TaskForm(ModelForm):
    title = forms.CharField(label='Judul task', max_length=255)
    description = forms.TextInput()
    class Meta:
        model = Task
        fields = ['title', 'description']