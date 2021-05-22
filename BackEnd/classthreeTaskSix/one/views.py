from django.http import HttpResponse
from django.shortcuts import render
# import math

def index(request):
    return HttpResponse("<h1>This is Index<h1>")

def triangle(request,a,b,c):
    s = (a + b + c) / 2
    area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
    return HttpResponse("Area {}".format(area))
def root(request,number):
    root=number**0.5
    return HttpResponse("Root {}".format(root))

def swap(request,number1,number2):
    number2,number1=number1,number2

    return HttpResponse('Swap of number2 {}'.format(number2))
