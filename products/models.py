"""Fruit Shop application - Products models file."""

from django.db import models
from django.conf import settings

# Create your models here.


class Product(models.Model):
    """Product model."""

    name = models.CharField(max_length=128)
    description = models.TextField(max_length=8192, blank=True)
    author_user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    time_created = models.DateTimeField(auto_now_add=True)
