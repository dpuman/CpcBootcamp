from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    if request.method=='GET':
        return render(request,'calc/form.html')
    if request.method=='POST':
        first_number=int(request.POST['u-first_number'])
        second_number=int(request.POST['u-second_number'])
        operator=request.POST['u-operator']
        result=0;
        if operator=='+':
            result=first_number+second_number
        elif operator=='-':
            result=first_number-second_number
        elif operator=='*':
            result=first_number*second_number
        elif operator=='/':
            result=first_number//second_number

        context={
            'result':result
        }

        return render(request,'calc/result.html',context)
