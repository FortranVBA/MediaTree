"""Fruit Shop application - Products views file."""

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import Product
import json

# Create your views here.
@login_required
def get_products_view(request):
    """Get the product main view."""
    if request.method == "GET":
        if "action" in request.GET:
            if request.GET.get("action") == "logout":
                if request.user.is_authenticated:
                    logout(request)
                    return redirect(reverse_lazy("login"))

    products = Product.objects.all()
    context = {"products": products}
    return render(request, "products/products.html", context)


@login_required
def API_products_create_list_view(request):
    """Get API entry point for all products listing and product create."""
    if request.method == "GET":
        products = Product.objects.all()
        data = serialize(
            "json",
            products,
            fields=("name", "description", "author_user", "time_created"),
        )
        return HttpResponse(data, content_type="application/json", status=200)

    elif request.method == "POST":
        body = json.loads(request.body)

        new_product = Product(
            name=body["name"],
            description=body["description"],
            user=request.user,
        )
        new_product.save()

        data = serialize(
            "json",
            [new_product],
            fields=("pk", "name", "description", "user", "time_created"),
        )
        return HttpResponse(data, content_type="application/json", status=201)

    else:
        return HttpResponse(
            "Error 405 : This method is not allowed for this url.", status=405
        )


@login_required
def API_products_update_delete_view(request, product):
    """Get API entry point for product partial update and product delete."""
    if request.method == "DELETE":
        breakpoint()
        return HttpResponse(
            "Error 405 : This method is not allowed for this url.", status=405
        )
    else:
        return HttpResponse(
            "Error 405 : This method is not allowed for this url.", status=405
        )
