"""Fruit Shop application - Users tests file."""

from django.test import TestCase
from django.urls import reverse


# Create your tests here.
class UsersTests(TestCase):
    """Users application test case."""

    def test_main_index(self):
        """Test connexion to the main index login page."""
        url = reverse("index")
        response = self.client.get(url)
        self.assertRedirects(response, reverse("login"))
