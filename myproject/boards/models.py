from django.db import models
from django.contrib.auth.models import User

class Board(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(null=True)
    description = models.TextField(max_length=4000)

    def __str__(self):
        return self.name
# Create your models here.
