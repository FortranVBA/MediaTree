"""Fruit Shop application - Users views file."""

from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .forms import FormLogin
from django.contrib.auth import authenticate, login
from django.contrib import messages


# Create your views here.
def get_login_view(request):
    """Get the user login view."""
    form_login = FormLogin()

    # Handle redirection if user is already authenticated
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect(reverse_lazy("products"))

    # Handle login submission
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
                    "Error : Name / password not matching",
                )

    context = {"form": form_login}
    return render(request, "users/login.html", context)


def get_index(request):
    """Get the default main view (that redirect to the login view)."""
    return redirect(reverse_lazy("login"))
