from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone

from task.models import Task, Tag


class TaskForm(forms.ModelForm):
    deadline_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        required=False
    )

    def clean_deadline_date(self):
        deadline_date = self.cleaned_data["deadline_date"]
        if deadline_date and deadline_date < timezone.now():
            raise ValidationError(
                "The deadline must be after the created date"
            )
        return deadline_date

    class Meta:
        model = Task
        fields = ("content", "deadline_date", "progres", "tags")


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "name",
