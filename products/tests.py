from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Product

class ProductListViewTests(TestCase):
    def setUp(self):
        # Create test data
        Product.objects.create(name='Product A', sku='SKU001', price=10.0)
        Product.objects.create(name='Product B', sku='SKU002', price=15.0)
        Product.objects.create(name='Product C', sku='SKU003', price=20.0)
        # Add more products as needed for testing

    def test_product_list(self):
        # Test retrieving the list of products
        client = APIClient()
        url = reverse('product-list')
        response = client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 3)  # Assuming 3 products were created in setUp

    def test_product_list_pagination(self):
        # Test pagination
        client = APIClient()
        url = reverse('product-list')
        response = client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('results', response.data)  # Check if results are paginated

    def test_product_list_filter_by_sku(self):
        # Test filtering by SKU
        client = APIClient()
        url = reverse('product-list')
        response = client.get(url, {'sku': 'SKU001'})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['sku'], 'SKU001')

    def test_product_list_order_by_sku(self):
        # Test ordering by SKU
        client = APIClient()
        url = reverse('product-list')
        response = client.get(url, {'ordering': 'sku'})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        skus = [product['sku'] for product in response.data['results']]
        self.assertEqual(skus, ['SKU001', 'SKU002', 'SKU003'])  # Assuming alphabetical order

