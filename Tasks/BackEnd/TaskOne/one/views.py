from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'one/index.html')
def home(request):
    return render(request,'one/home.html')
def about(request):
    return render(request,'one/about.html')
def contact(request):
    return render(request,'one/contact.html')