"""Fruit Shop application - Products url file."""

from django.conf.urls import url

from .views import get_products_view


urlpatterns = [
    url(r"^$", get_products_view, name="products"),
]
