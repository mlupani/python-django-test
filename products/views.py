from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import Product

def index(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'products/index.html', context)

def detail(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {
        'product': product
    }
    return render(request, 'products/detail.html', context)