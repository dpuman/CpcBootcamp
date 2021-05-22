from django.shortcuts import redirect, render
from django.http import HttpResponse
from pharmasite.models import Products, GetInTouch
from django.urls import reverse

# Create your views here.


def index(request):
    products = Products.objects.all()

    context = {
        'products': products
    }
    return render(request, 'index.html', context)


def products(request):
    products = Products.objects.all()

    context = {
        'products': products
    }
    return render(request, 'shop.html', context)


def selected_product(request, medicine_name):
    selected_product = Products.objects.get(slug=medicine_name)
    return render(request, "shop-single.html", {'selected_product': selected_product})


def search(request):
    product = request.GET['query']
    selected_product = Products.objects.get(name=product)
    return render(request, "shop-single.html", {'selected_product': selected_product})


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'GET':

        return render(request, 'contact.html')

    elif request.method == 'POST':
        fname = request.POST['c_fname']
        lname = request.POST['c_lname']
        email = request.POST['c_email']
        subject = request.POST['c_subject']
        message = request.POST['c_message']

        get_in_touct = GetInTouch(
            first_name=fname, last_name=lname, email=email, subject=subject, message=message)
        get_in_touct.save()
        return redirect('contact')
