"""Fruit Shop application - Sells views file."""

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect, render
from django.urls import reverse_lazy


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

    context = {}
    return render(request, "sells/sells.html", context)
