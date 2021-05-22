from django.shortcuts import render

def home(request,a,b):
    sum=a+b;
    context={
        "first_variable":a,
        'second_variable':b,
        'Summation':sum,
    }

    return render(request,'addition/home.html',context)
