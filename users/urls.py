"""Fruit Shop application - Users url file."""

from django.conf.urls import url

from .views import get_login_view


urlpatterns = [
    url(r"^login/", get_login_view, name="login"),
]
