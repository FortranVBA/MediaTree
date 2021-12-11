"""Fruit Shop application - Sells tests file."""

from django.test import TestCase
from django.urls import reverse
import json


# Create your tests here.
class UsersTests(TestCase):
    """Products application test case."""

    fixtures = ["users_data.json", "products_data.json", "sells_data.json"]

    def test_sells_index_without_login(self):
        """Test connexion to the sells index without login."""
        url = reverse("sells")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_sells_index(self):
        """Test connexion to the sells index."""
        self.client.login(username="admin", password="admin")
        url = reverse("sells")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_API_sell_list_without_login(self):
        """Test the API sell list entry point without login."""
        url = reverse("APIsells")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_API_sell_list(self):
        """Test the API sell list entry point."""
        self.client.login(username="admin", password="admin")
        url = reverse("APIsells")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_API_sell_create_without_login(self):
        """Test the API sell create entry point without login."""
        url = reverse("APIsells")
        data = {"product": 1, "quantity": 5}
        response = self.client.post(
            url, json.dumps(data), content_type="application/json"
        )
        self.assertEqual(response.status_code, 302)

    def test_API_sell_create(self):
        """Test the API sell create entry point."""
        self.client.login(username="admin", password="admin")
        url = reverse("APIsells")
        data = {"product": 1, "quantity": 5}
        response = self.client.post(
            url, json.dumps(data), content_type="application/json"
        )
        self.assertEqual(response.status_code, 201)

    def test_API_sell_create_with_blank_quantity(self):
        """Test the API sell create entry point with blank quantity."""
        self.client.login(username="admin", password="admin")
        url = reverse("APIsells")
        data = {"product": 1, "quantity": ""}
        response = self.client.post(
            url, json.dumps(data), content_type="application/json"
        )
        self.assertEqual(response.status_code, 400)

    def test_API_sell_create_with_negative_quantity(self):
        """Test the API sell create entry point with negative number as quantity."""
        self.client.login(username="admin", password="admin")
        url = reverse("APIsells")
        data = {"product": 1, "quantity": -5}
        response = self.client.post(
            url, json.dumps(data), content_type="application/json"
        )
        self.assertEqual(response.status_code, 400)

    def test_API_sell_patch_without_login(self):
        """Test the API sell patch entry point without login."""
        url = reverse("APIsellsDetails", kwargs={"sell": 2})
        data = {"product": 1, "quantity": 6}
        response = self.client.patch(
            url, json.dumps(data), content_type="application/json"
        )
        self.assertEqual(response.status_code, 302)

    def test_API_sell_patch(self):
        """Test the API sell patch entry point."""
        self.client.login(username="admin", password="admin")
        url = reverse("APIsellsDetails", kwargs={"sell": 2})
        data = {"product": 1, "quantity": 6}
        response = self.client.patch(
            url, json.dumps(data), content_type="application/json"
        )
        self.assertEqual(response.status_code, 204)

    def test_API_sell_delete_without_login(self):
        """Test the API sell delete entry point without login."""
        url = reverse("APIsellsDetails", kwargs={"sell": 2})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 302)

    def test_API_sell_delete(self):
        """Test the API sell delete entry point."""
        self.client.login(username="admin", password="admin")
        url = reverse("APIsellsDetails", kwargs={"sell": 2})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
