from django.test import TestCase
from django.utils import timezone
from task.forms import TaskForm, TagForm
from task.models import Tag


class TaskFormTest(TestCase):
    def test_valid_form(self):
        form_data = {
            "content": "Test Task",
            "deadline_date": timezone.now(),
            "progres": False,
        }
        form = TaskForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_deadline_date(self):
        form_data = {
            "content": "Test Task",
            "deadline_date": timezone.now() - timezone.timedelta(days=1),
            "progres": False,
        }
        form = TaskForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("deadline_date", form.errors)


class TagFormTest(TestCase):
    def test_valid_form(self):
        form_data = {
            "name": "Test Tag",
        }
        form = TagForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_name(self):
        form_data = {
            "name": "",
        }
        form = TagForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("name", form.errors)
