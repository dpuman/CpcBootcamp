from django.shortcuts import render
from .models import Blog
# Create your views here.


def home(request):
    blogs = Blog.objects.all()
    contex = {
        'blogs': blogs
    }
    return render(request, 'main/index.html', contex)
