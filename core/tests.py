from django.test import TestCase
from django.urls import reverse
from .models import Product, Order

class ProductModelTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name="Test Product",
            price=29.99,
            description="Test Description"
        )
    
    def test_product_creation(self):
        self.assertEqual(self.product.name, "Test Product")
        self.assertEqual(self.product.price, 29.99)
        self.assertEqual(self.product.description, "Test Description")

class OrderModelTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name="Test Product",
            price=10.00,
            description="Test Description"
        )
    
    def test_order_creation(self):
        order = Order(product=self.product, quantity=3)
        order.save()
        self.assertEqual(order.total_price, 30.00)

class ViewTests(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name="Test Product",
            price=15.50,
            description="Test Description"
        )
    
    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {'message': 'Welcome to Django CI/CD Project', 'status': 'success'}
        )
    
    def test_products_list_view(self):
        response = self.client.get(reverse('products_list'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('products', response.json())
    
    def test_create_order_view(self):
        response = self.client.get(f'/order/{self.product.id}/2/')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['message'], 'Order created successfully')
        self.assertEqual(float(data['total_price']), 31.00)
    
    def test_create_order_invalid_product(self):
        response = self.client.get('/order/999/2/')
        self.assertEqual(response.status_code, 404)