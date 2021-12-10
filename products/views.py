"""Fruit Shop application - Products views file."""

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import Product

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

    context = {}
    return render(request, "products/products.html", context)


@login_required
def API_products_create_list_view(request):
    """List all products."""

    if request.method == "GET":
        products = Product.objects.all()
        data = serialize(
            "json", products, fields=("name", "description", "user", "time_created")
        )
        return HttpResponse(data, content_type="application/json")
    elif request.method == "POST":
        breakpoint()
        new_product = Product(
            name=request.body["name"],
            description=request.body["description"],
            user=request.user,
        )
        new_product.save()
    else:
        return HttpResponse("Error 405 : This method is not allowed for this url.")
