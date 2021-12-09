"""Fruit Shop application - Users views file."""

from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .forms import FormLogin
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.


def get_login_view(request):
    """Get the user login view."""
    form_login = FormLogin()

    if request.method == "GET":
        if "action" in request.GET:
            action = request.GET.get("action")
            if action == "logout":
                if request.user.is_authenticated:
                    logout(request)

        if request.user.is_authenticated:
            return redirect(reverse_lazy("products"))

    if request.method == "POST":
        form_login = FormLogin(request.POST)
        if form_login.is_valid():
            username = form_login.cleaned_data["username"]
            password = form_login.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect(reverse_lazy("products"))
            else:
                messages.add_message(
                    request,
                    messages.INFO,
                    "Name / password not matching",
                )

    context = {"form": form_login}
    return render(request, "users/login.html", context)


def get_index(request):
    """Get the default main view."""
    return redirect(reverse_lazy("login"))
