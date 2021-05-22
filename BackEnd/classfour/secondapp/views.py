from django.shortcuts import render

# Create your views here.
def home(request):
    contaxt={
        'name':'Sadman Sakib',
        'ffood':'Pizza',
        'age':'23'
    }
    return render(request,'secondapp/home.html',contaxt)