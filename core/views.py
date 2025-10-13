from django.shortcuts import render
from django.http import JsonResponse
from .models import Product, Order

def home(request):
    return JsonResponse({
        'message': 'Welcome to Django CI/CD Project',
        'status': 'success'
    })

def products_list(request):
    products = Product.objects.all()
    data = [
        {
            'id': product.id,
            'name': product.name,
            'price': str(product.price),
            'description': product.description
        }
        for product in products
    ]
    return JsonResponse({'products': data})

def create_order(request, product_id, quantity):
    try:
        product = Product.objects.get(id=product_id)
        order = Order(product=product, quantity=quantity)
        order.save()
        return JsonResponse({
            'message': 'Order created successfully',
            'order_id': order.id,
            'total_price': str(order.total_price)
        })
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product not found'}, status=404)