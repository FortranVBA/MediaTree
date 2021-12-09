"""Fruit Shop application - Users forms file."""

from django import forms


class FormLogin(forms.Form):
    """User login form."""

    username = forms.CharField(label=("Username"), required=True)
    password = forms.CharField(
        label=("Password"), required=True, widget=forms.PasswordInput()
    )
