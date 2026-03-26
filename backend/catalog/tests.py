from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Category, Product


class ProductModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Elettronica")

    def test_product_creation(self):
        """Verifica che un prodotto venga creato correttamente"""
        p = Product.objects.create(name="Mouse", price=20.50, category=self.category)
        self.assertEqual(p.name, "Mouse")
        self.assertEqual(float(p.price), 20.50)

class ProductAPITest(APITestCase):
    def setUp(self):
        self.cat = Category.objects.create(name="Elettronica")
        Product.objects.create(name="Laptop", price=1000, category=self.cat)
        Product.objects.create(name="Smartphone", price=500, category=self.cat)

    def test_get_products_list(self):
        """Verifica che la lista prodotti funzioni"""
        url = reverse('product-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)

    def test_filter_price_min(self):
        """Verifica il filtro prezzo minimo"""
        url = reverse('product-list')
        response = self.client.get(url, {'min_price': 600})
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['name'], "Laptop")

    def test_create_invalid_price(self):
        """Verifica che non si possa creare un prodotto con prezzo negativo (Validazione)"""
        url = reverse('product-list')
        data = {"name": "Test", "price": -10, "category_id": self.cat.id}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
