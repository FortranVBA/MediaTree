"""Fruit Shop application - Products tests file."""

from django.test import TestCase
from django.urls import reverse
import json


# Create your tests here.
class ProductsTests(TestCase):
    """Products application test case."""

    fixtures = ["users_data.json", "products_data.json"]

    def test_products_index_without_login(self):
        """Test connexion to the products index without login."""
        url = reverse("products")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_products_index(self):
        """Test connexion to the products index."""
        self.client.login(username="admin", password="admin")
        url = reverse("products")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_API_product_list_without_login(self):
        """Test the API product list entry point without login."""
        url = reverse("APIproducts")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_API_product_list(self):
        """Test the API product list entry point."""
        self.client.login(username="admin", password="admin")
        url = reverse("APIproducts")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_API_product_create_without_login(self):
        """Test the API product create entry point without login."""
        url = reverse("APIproducts")
        data = {"name": "New product", "description": "Test product description"}
        response = self.client.post(
            url, json.dumps(data), content_type="application/json"
        )
        self.assertEqual(response.status_code, 302)

    def test_API_product_create(self):
        """Test the API product create entry point."""
        self.client.login(username="admin", password="admin")
        url = reverse("APIproducts")
        data = {"name": "New product", "description": "Test product description"}
        response = self.client.post(
            url, json.dumps(data), content_type="application/json"
        )
        self.assertEqual(response.status_code, 201)

    def test_API_product_create_with_blank_name(self):
        """Test the API product create entry point with a blank name."""
        self.client.login(username="admin", password="admin")
        url = reverse("APIproducts")
        data = {"name": "", "description": "Test product description"}
        response = self.client.post(
            url, json.dumps(data), content_type="application/json"
        )
        self.assertEqual(response.status_code, 400)

    def test_API_product_patch_without_login(self):
        """Test the API product patch entry point without login."""
        url = reverse("APIproductsDetails", kwargs={"product": 2})
        data = {"name": "Updated product", "description": "Updated description"}
        response = self.client.patch(
            url, json.dumps(data), content_type="application/json"
        )
        self.assertEqual(response.status_code, 302)

    def test_API_product_patch(self):
        """Test the API product patch entry point."""
        self.client.login(username="admin", password="admin")
        url = reverse("APIproductsDetails", kwargs={"product": 2})
        data = {"name": "Updated product", "description": "Updated description"}
        response = self.client.patch(
            url, json.dumps(data), content_type="application/json"
        )
        self.assertEqual(response.status_code, 204)

    def test_API_product_delete_without_login(self):
        """Test the API product delete entry point without login."""
        url = reverse("APIproductsDetails", kwargs={"product": 2})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 302)

    def test_API_product_delete(self):
        """Test the API product delete entry point."""
        self.client.login(username="admin", password="admin")
        url = reverse("APIproductsDetails", kwargs={"product": 2})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
