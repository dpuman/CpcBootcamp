from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>This is Home</h1>")

def evenodd(request,number):
    if (number%2)==0:
        return HttpResponse("{} is Even".format(number))

    else:
        return HttpResponse("{} is Odd".format(number))