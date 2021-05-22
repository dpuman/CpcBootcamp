from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'thirdapp/home.html')
def about(request):
    return render(request,'thirdapp/about.html')
def contact(request):
    return render(request,'thirdapp/contact.html')