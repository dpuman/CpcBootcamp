from django.shortcuts import render



def home(request):
    contaxt={
        'name':'Dipankar Barman',
        'ffood':'Burger',
        'age':'23'
    }
    return render(request,'firstapp/home.html',contaxt)