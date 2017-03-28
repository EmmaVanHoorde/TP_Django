from django import forms
from todo.models import Task

class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        #fields = ('created_by','name', 'description',)
        fields = '__all__'
