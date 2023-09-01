from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    deadline_date = models.DateTimeField(null=True, blank=True)
    progres = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="tasks", blank=True)

    def __str__(self) -> str:
        return self.content

    class Meta:
        ordering = ["progres", "-created_date"]
