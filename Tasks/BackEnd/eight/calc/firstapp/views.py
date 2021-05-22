from django.http import HttpResponse
from django.shortcuts import render

def sum(request,a,b):
    result=a+b

    context={
        'a':a,
        'b':b,
        'result':result
    }

    return render(request,'firstapp/index.html',context)

def sub(request,a,b):
    result=a-b

    context={
        'a':a,
        'b':b,
        'result':result
    }

    return render(request,'firstapp/index.html',context)

def multi(request,a,b):
    result=a*b

    context={
        'a':a,
        'b':b,
        'result':result
    }

    return render(request,'firstapp/index.html',context)
def div(request,a,b):
    result=a//b

    context={
        'a':a,
        'b':b,
        'result':result
    }

    return render(request,'firstapp/index.html',context)