"""Fruit Shop application - Sells views file."""

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.core.serializers import serialize
from django.http import HttpResponse
from django.db.models import Sum
from products.models import Product
from .models import Sell
import json


# Create your views here.
@login_required
def get_sells_view(request):
    """Get the sell main view."""
    if request.method == "GET":
        if "action" in request.GET:
            if request.GET.get("action") == "logout":
                if request.user.is_authenticated:
                    logout(request)
                    return redirect(reverse_lazy("login"))

    products = Product.objects.all()
    sells = Sell.objects.all()

    total_table = []
    for product in products:
        total_sells = Sell.objects.filter(product=product).aggregate(Sum("quantity"))[
            "quantity__sum"
        ]
        if not total_sells:
            total_sells = 0
        total_table.append(
            {
                "id": product.pk,
                "product": product.name,
                "quantity": total_sells,
            }
        )

    context = {
        "products": products,
        "sells": sells,
        "total_table": total_table,
    }

    return render(request, "sells/sells.html", context)


@login_required
def API_sells_create_list_view(request):
    """Get API entry point for all sells listing and sell create."""
    if request.method == "GET":
        sells = Sell.objects.all()
        data = serialize(
            "json",
            sells,
            fields=("product", "quantity", "author_user", "time_last_updated"),
        )
        return HttpResponse(data, content_type="application/json", status=200)

    elif request.method == "POST":
        body = json.loads(request.body)

        product_sold = Product.objects.get(pk=body["product"])
        new_sell = Sell(
            product=product_sold,
            quantity=body["quantity"],
            author_user=request.user,
        )
        new_sell.save()

        data = serialize(
            "json",
            [new_sell],
            fields=("pk", "product", "quantity", "author_user", "time_last_updated"),
        )
        return HttpResponse(data, content_type="application/json", status=201)

    else:
        return HttpResponse(
            "Error 405 : This method is not allowed for this url.", status=405
        )


@login_required
def API_sells_update_delete_view(request, sell):
    """Get API entry point for sell partial update and sell delete."""
    if request.method == "PATCH":
        sell_content = Sell.objects.get(pk=sell)

        if sell_content:
            body = json.loads(request.body)

            if body["product"]:
                product_sold = Product.objects.get(pk=body["product"])
                sell_content.product = product_sold
            if body["quantity"]:
                sell_content.quantity = body["quantity"]
            sell_content.author_user = request.user

            sell_content.save()

            return HttpResponse("Object updated.", status=204)

        return HttpResponse("Object not found.", status=404)

    elif request.method == "DELETE":
        sell_content = Sell.objects.get(pk=sell)

        if sell_content:
            sell_content.delete()

            return HttpResponse("Object deleted.", status=204)

        return HttpResponse("Object not found.", status=404)

    else:
        return HttpResponse(
            "Error 405 : This method is not allowed for this url.", status=405
        )
