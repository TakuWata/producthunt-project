from django.shortcuts import render
from .models import Product


def home(request):
  return render(request, 'product/home.html')


def product(request):
  products = Product.ojbects
  return render(request, 'product/product.html', {'products': products})
