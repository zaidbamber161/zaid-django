from django.db import models
from django.utils import timezone
import datetime


class MyNotes(models.Model):
    title = models.CharField(max_length=60, blank=False)
    description = models.TextField(max_length=300, blank=False)
    note_created_date = models.DateField('Date published')
    is_read = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
