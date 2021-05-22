from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages, auth
from .models import ShortUrl
# from .forms import CreateShortUrl, CreateUserForm
import random
import string

from django.contrib.auth.models import User

# Create your views here.


def login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            # handle login
            if request.POST['email'] and request.POST['password']:
                try:
                    user = User.objects.get(email=request.POST['email'])
                    auth.login(request, user)
                    if request.POST['next'] != '':
                        return redirect(request.POST.get('next'))
                    else:
                        return redirect('/')
                    return redirect('/')
                except User.DoesNotExist:
                    return render(request, 'shortner/login.html', {'error': "User Doesn't Exist"})
            else:
                return render(request, 'shortner/login.html', {'error': "Empty Fields"})
        else:
            return render(request, 'shortner/login.html')
    else:
        return redirect('/')


def signup(request):
    if request.method == "POST":
        # handle sign in
        if request.POST['password'] == request.POST['password2']:
            if request.POST['username'] and request.POST['email'] and request.POST['password']:
                try:
                    user = User.objects.get(email=request.POST['email'])
                    return render(request, 'shortner/signup.html', {'error': "User Already Exists"})
                except User.DoesNotExist:
                    User.objects.create_user(
                        username=request.POST['username'],
                        email=request.POST['email'],
                        password=request.POST['password'],
                    )
                    messages.success(
                        request, "Signup Successful <br> Login Here")
                    return redirect(login)
            else:
                return render(request, 'shortner/signup.html', {'error': "Empty Fields"})
        else:
            return render(request, 'shortner/signup.html', {'error': "Password's Don't Match"})
    else:
        return render(request, 'shortner/signup.html')


def logout(request):
    auth.logout(request)
    return redirect('/login')


@login_required(login_url='/login/')
def shortner(request):
    usr = request.user
    urls = ShortUrl.objects.filter(user=usr)
    return render(request, 'shortner/shortner.html', {'urls': urls})


def randomgen():
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(6))


@login_required(login_url='/login/')
def generate(request):
    if request.method == "POST":
        # generate
        pass
        if request.POST['original'] and request.POST['short']:
            # generate based on user input
            usr = request.user
            original = request.POST['original']
            short = request.POST['short']
            check = ShortUrl.objects.filter(short_query=short)
            if not check:
                newurl = ShortUrl(
                    user=usr,
                    original_url=original,
                    short_query=short,
                )
                newurl.save()
                return redirect(shortner)
            else:
                messages.error(request, "Already Exists")
                return redirect(shortner)
        elif request.POST['original']:
            # generate randomly
            usr = request.user
            original = request.POST['original']
            generated = False
            while not generated:
                short = randomgen()
                check = ShortUrl.objects.filter(short_query=short)
                if not check:
                    newurl = ShortUrl(
                        user=usr,
                        original_url=original,
                        short_query=short,
                    )
                    newurl.save()
                    return redirect(shortner)
                else:
                    continue
        else:
            messages.error(request, "Empty Fields")
            return redirect(shortner)
    else:
        return redirect('/shortner')


def home(request, query=None):
    if not query or query is None:
        return render(request, 'shortner/home.html')
    else:
        try:
            check = ShortUrl.objects.get(short_query=query)
            check.visits = check.visits + 1
            check.save()
            url_to_redirect = check.original_url
            return redirect(url_to_redirect)
        except ShortUrl.DoesNotExist:
            return render(request, 'shortner/home.html', {'error': "error"})

# added delete URl


@login_required(login_url='/login/')
def deleteurl(request):
    if request.method == "POST":
        short = request.POST['delete']
        try:
            check = ShortUrl.objects.filter(short_query=short)
            check.delete()
            return redirect(shortner)
        except ShortUrl.DoesNotExist:
            return redirect(home)
    else:
        return redirect(home)
