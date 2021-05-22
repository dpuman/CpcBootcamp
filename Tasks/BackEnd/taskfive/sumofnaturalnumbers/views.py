from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>This iS My HOme</h1>")

def sumofnaturalnum(request,number):
    sum=0;
    for i in range(0,number+1):
        sum+=i

    return HttpResponse("The sum of natural numbers up to {} is {}".format(number,sum))
