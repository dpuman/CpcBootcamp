from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    return HttpResponse("<h1>This is Index<h1>")

def sum(request,a,b):
    sum = a+b
    return HttpResponse("Summetion {}".format(sum))
def sub(request,a,b):
    sub = a-b
    return HttpResponse("Subtraction {}".format(sub))

