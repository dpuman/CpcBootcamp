from django.http import HttpResponse
from django.shortcuts import render

# home, about, contact
def index(request):
    return HttpResponse('This is the Index')

def home(request):
    return render(request,'firstapplication/home.html')
def about(request):
    return render(request,'firstapplication/about.html')
def contact(request):
    return render(request,'firstapplication/contact.html')