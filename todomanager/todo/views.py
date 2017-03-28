from django.shortcuts import render


# Create your views here.
from django.views.generic import ListView
from todo.models import Task
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from todo.forms import TaskCreateForm

class TaskListView(ListView):
    """Documentation de notre controleur"""
    model = Task
    context_object_name = "tasks"
    template_name = "todo/tasks-list.html"
    paginate_by = None

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskCreateForm
    template_name = "todo/tasks-form.html"

    def get_initial(self):
        return {'created_by': self.request.user.member,
                'modified_by': self.request.user.member,
                'assigned_to': self.request.user.member}

class TaskRetrieveView(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = "todo/tasks-details.html"

class TaskUpdateView(UpdateView):
    model = Task
    context_object_name = 'task'
    template_name = "todo/tasks-form.html"
    form_class = TaskCreateForm
    def get_initial(self):
        return {
                'modified_by': self.request.user.member,
                'assigned_to': self.request.user.member
                }

class TaskDeleteView(DeleteView):
    model = Task
    context_object_name = 'tasks'
    template_name = "todo/tasks-delete.html"
    success_url = '/'
