from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'secondapp/home.html')
def about(request):
    return render(request,'secondapp/about.html')
def contact(request):
    return render(request,'secondapp/contact.html')

# Create your views here.
