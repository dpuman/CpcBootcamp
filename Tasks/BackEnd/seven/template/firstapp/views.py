from django.shortcuts import render

# Create your views here.
def home(request):

    if request.method=='GET':
        return render(request,'firstapp/formhome.html')

    if request.method=='POST':
        name=request.POST['u-name']
        type=request.POST['u-types']
        copyright=request.POST['u-copyright']
        details=request.POST['u-details']

        context={
            'name':name,
            'type':type,
            'copyright':copyright,
            'details':details
        }
        return render(request,'firstapp/home.html',context)


def about(request):
    if request.method=='GET':
        return render(request,'firstapp/formabout.html')
    if request.method=='POST':


        context={
            'name':request.POST['u-name'],
            'email': request.POST['u-email'],
            'address': request.POST['u-address'],
            'phone_number': request.POST['u-tel'],
            'birth_date':request.POST['u-date'],
            'gender':request.POST['gender']
        }

        return render(request,'firstapp/about.html',context)