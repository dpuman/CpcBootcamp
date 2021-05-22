from django.shortcuts import redirect, render
from django.http import HttpResponse
from .form import CreateUserForm
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required
# Create your views he


def register(request):
    if request.user.is_authenticated:
        return redirect('user')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

        context = {'form': form}
        return render(request, 'user/register.html', context)


def loginPage(request):

    if request.user.is_authenticated:
        return redirect('user')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('user')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'user/login.html', context)


@login_required(login_url='login')
def user(request):

    user = request.user

    return render(request, 'user/user.html', {"user": user})


def logoutUser(request):
    logout(request)
    return redirect('login')
