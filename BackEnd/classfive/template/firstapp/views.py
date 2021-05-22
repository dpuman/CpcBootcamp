from django.shortcuts import render

# Create your views here.

def form(request):
    name=request.GET.get('u-name')
    email=request.GET.get('u-email')

    context= {
        'name':name,
        'email':email

    }

    return render(request,'firstapp/form.html',context)

def getpost(request):
    if request.method=='GET':
        return render(request,'firstapp/post.html')

    if request.method=='POST':
        name=request.POST['u-name']
        email=request.POST['u-email']
        password=request.POST['u-password']

        context={
            'name':name,
            'email':email,
            'password':password
        }

        return render(request,'firstapp/data.html',context)


def sum(request):
    if request.method=='GET':
        return render(request,'firstapp/sum.html')

    if request.method=='POST':
        fnumber=int(request.POST['u-fnumber'])
        snumber=int(request.POST['u-snumber'])

        result=fnumber+snumber

        contex={
            'result':result
        }
        return render(request,'firstapp/sum.html',contex)