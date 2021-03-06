"""Fruit Shop application - Products url file."""

from django.conf.urls import url

from .views import (
    get_products_view,
    API_products_create_list_view,
    API_products_update_delete_view,
)


urlpatterns = [
    url(r"^index/", get_products_view, name="products"),
    url(r"^$", API_products_create_list_view, name="APIproducts"),
    url(
        r"^(?P<product>[0-9]+)$",
        API_products_update_delete_view,
        name="APIproductsDetails",
    ),
]
