from django.db import models

from .base import BaseModel

class Note(BaseModel):
    topic = models.ForeignKey('Topic', related_name='notes')
    notes = models.CharField(max_length=128)

    class Meta:
        verbose_name = "note"
        verbose_name_plural = "notes"
        ordering = ['topic', 'notes']