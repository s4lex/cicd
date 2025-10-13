from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products_list, name='products_list'),
    path('order/<int:product_id>/<int:quantity>/', views.create_order, name='create_order'),
]