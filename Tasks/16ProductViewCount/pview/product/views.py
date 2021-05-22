from django.shortcuts import render
from .models import Product
import time
# Create your views here.


def index(request):
    products = Product.objects.order_by('-view_count')
    context = {
        'products': products
    }
    return render(request, 'product/index.html', context)


def productView(request, id):
    product = Product.objects.get(id=id)
    product.view_count = product.view_count+1
    product.save()
    # time.sleep(3)

    context = {
        'product': product
    }
    return render(request, 'product/product.html', context)
