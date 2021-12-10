"""Fruit Shop application - Sells url file."""

from django.conf.urls import url

from .views import (
    get_sells_view,
    API_sells_create_list_view,
    API_sells_update_delete_view,
)


urlpatterns = [
    url(r"^index/", get_sells_view, name="sells"),
    url(r"^$", API_sells_create_list_view, name="APIsells"),
    url(
        r"^(?P<sell>[0-9]+)$",
        API_sells_update_delete_view,
        name="APIsellsDetails",
    ),
]
