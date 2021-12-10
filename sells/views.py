"""Fruit Shop application - Sells views file."""

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.core.serializers import serialize
from django.http import HttpResponse
from products.models import Product
from .models import Sell
import json

# Create your views here.
@login_required
def get_sells_view(request):
    """Get the product main view."""
    if request.method == "GET":
        if "action" in request.GET:
            if request.GET.get("action") == "logout":
                if request.user.is_authenticated:
                    logout(request)
                    return redirect(reverse_lazy("login"))

    products = Product.objects.all()
    sells = Sell.objects.all()
    context = {"products": products, "sells": sells}
    return render(request, "sells/sells.html", context)


@login_required
def API_sells_create_list_view(request):
    """Get API entry point for all sells listing and sell create."""
    if request.method == "GET":
        products = Sell.objects.all()
        data = serialize(
            "json",
            products,
            fields=("name", "description", "author_user", "time_last_updated"),
        )
        return HttpResponse(data, content_type="application/json", status=200)

    else:
        return HttpResponse(
            "Error 405 : This method is not allowed for this url.", status=405
        )
