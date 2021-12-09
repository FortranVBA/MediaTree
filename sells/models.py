"""Fruit Shop application - Sells models file."""

from django.db import models
from products.models import Product
from django.conf import settings

# Create your models here.


class Review(models.Model):
    """Review model."""

    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)
