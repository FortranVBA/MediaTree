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
            fields=("name", "description", "author_user", "time_last_updated"),
        )
        return HttpResponse(data, content_type="application/json", status=200)

    elif request.method == "POST":
        body = json.loads(request.body)

        if not body["name"]:
            return HttpResponse("Product name cannot be empty.", status=400)

        new_product = Product(
            name=body["name"],
            description=body["description"],
            author_user=request.user,
        )
        new_product.save()

        data = serialize(
            "json",
            [new_product],
            fields=("pk", "name", "description", "author_user", "time_last_updated"),
        )
        return HttpResponse(data, content_type="application/json", status=201)

    else:
        return HttpResponse(
            "Error 405 : This method is not allowed for this url.", status=405
        )


@login_required
def API_products_update_delete_view(request, product):
    """Get API entry point for product partial update and product delete."""
    if request.method == "PATCH":
        product_content = Product.objects.get(pk=product)

        if product_content:
            body = json.loads(request.body)

            if body["name"]:
                product_content.name = body["name"]
            product_content.description = body["description"]
            product_content.author_user = request.user

            product_content.save()

            return HttpResponse("Object updated.", status=204)

        return HttpResponse("Object not found.", status=404)

    elif request.method == "DELETE":
        product_content = Product.objects.get(pk=product)

        if product_content:
            product_content.delete()

            return HttpResponse("Object deleted.", status=204)

        return HttpResponse("Object not found.", status=404)

    else:
        return HttpResponse(
            "Error 405 : This method is not allowed for this url.", status=405
        )
