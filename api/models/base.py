from django.db import models
from uuid import uuid4


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True
