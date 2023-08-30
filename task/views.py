from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic, View

from task.forms import TagForm, TaskForm
from task.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    template_name = "task/task_list.html"
    queryset = Task.objects.prefetch_related("tags")


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task:task-list")


class TaskUpdateFormView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("task:task-list")


class ChangeTaskProgresView(View):
    def post(self, request, pk, *args, **kwargs):
        task = Task.objects.get(pk=pk)

        task.progres = not task.progres
        task.save()

        return HttpResponseRedirect(
            reverse_lazy("task:task-list")
        )


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("task:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("task:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("task:tag-list")
