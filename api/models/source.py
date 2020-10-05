from django.db import models

from .base import BaseModel

class Source(BaseModel):
    name = models.CharField(max_length=128)

    class Meta:
        verbose_name = "source"
        verbose_name_plural = "sources"
