from django.test import TestCase

from django.test import TestCase
from task.models import Tag, Task
from datetime import datetime


class TagModelTest(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(name='Test Tag')

    def test_tag_name(self):
        self.assertEqual(str(self.tag), 'Test Tag')


class TaskModelTest(TestCase):
    def setUp(self):
        self.tag1 = Tag.objects.create(name='Tag 1')
        self.tag2 = Tag.objects.create(name='Tag 2')
        self.task = Task.objects.create(content='Test Task', deadline_date=datetime.now())
        self.task.tags.add(self.tag1, self.tag2)

    def test_task_content(self):
        self.assertEqual(str(self.task), 'Test Task')

    def test_task_deadline_date(self):
        self.assertIsNotNone(self.task.deadline_date)

    def test_task_progress_default(self):
        self.assertFalse(self.task.progres)

    def test_task_tags(self):
        self.assertIn(self.tag1, self.task.tags.all())
        self.assertIn(self.tag2, self.task.tags.all())

    def test_task_with_no_deadline(self):
        task_without_deadline = Task.objects.create(content='Task without deadline')
        self.assertIsNone(task_without_deadline.deadline_date)
