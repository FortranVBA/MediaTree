"""Fruit Shop application - Sells url file."""

from django.conf.urls import url

from .views import get_sells_view


urlpatterns = [
    url(r"^$", get_sells_view, name="sells"),
]
