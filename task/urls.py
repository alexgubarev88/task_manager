from django.urls import path

from task.views import TaskListView, TaskCreateView, TaskUpdateFormView, TaskDeleteView, ChangeTaskProgresView, \
    TagListView, TagCreateView, TagUpdateView, TagDeleteView

urlpatterns = [
    path('', TaskListView.as_view(), name="task-list"),
    path("create/", TaskCreateView.as_view(), name="task-create"),
    path("<int:pk>/update", TaskUpdateFormView.as_view(), name="task-update"),
    path("<int:pk>/delete", TaskDeleteView.as_view(), name="task-delete"),
    path("<int:pk>/change_progres/", ChangeTaskProgresView.as_view(), name="task-change-progres"),
    path("tag/", TagListView.as_view(), name="tag-list"),
    path("tag/create/", TagCreateView.as_view(), name="tag-create"),
    path("tag/<int:pk>/update", TagUpdateView.as_view(), name="tag-update"),
    path("tag/<int:pk>/delete", TagDeleteView.as_view(), name="tag-delete"),
]

app_name = 'task'
