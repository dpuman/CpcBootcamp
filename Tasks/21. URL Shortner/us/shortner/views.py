from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages, auth
from .models import ShortUrl, CustomUser
from .forms import CreateUserForm, CreateCustomUser
import random
import string

from django.contrib.auth.models import User
from datetime import datetime, timedelta
# Create your views here.


def signup(request):

    form = CreateUserForm()
    form_p = CreateCustomUser()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        form_p = CreateCustomUser(request.POST)
        if form.is_valid() and form_p.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            account_type = form_p.cleaned_data.get('account_type')

            # Added username after video because of error returning customer name if not added
            CustomUser.objects.create(
                my_user=user,
                account_type=account_type,
            )

            messages.success(request, 'Account was created for ' + username)

            return redirect('login')

    context = {'form': form, 'form_p': form_p}
    return render(request, 'shortner/signup-copy.html', context)


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
            time = request.POST['time']
            check = ShortUrl.objects.filter(short_query=short)
            counter = request.user.shorturl_set.filter().count()
            print(counter)
            if not check:
                newurl = ShortUrl(
                    user=usr,
                    original_url=original,
                    short_query=short,
                    expire_date=time
                )
                if request.user.customuser.account_type:
                    newurl.save()
                    print("Premium hello bangladesh how are you")
                    return redirect(shortner)

                elif counter <= 50:
                    print("Not P hello bangladesh how are you")
                    newurl.save()
                    return redirect(shortner)

            else:
                messages.error(request, "Already Exists")
                return redirect(shortner)
        elif request.POST['original']:
            # generate randomly
            usr = request.user
            original = request.POST['original']
            time = request.POST['time']
            if not time:
                time = datetime.now() + timedelta(days=30)

            print(time)
            counter = request.user.shorturl_set.filter().count()
            generated = False
            while not generated:
                short = randomgen()
                check = ShortUrl.objects.filter(short_query=short)
                if not check:
                    newurl = ShortUrl(
                        user=usr,
                        original_url=original,
                        short_query=short,
                        expire_date=time
                    )
                    if request.user.customuser.account_type:
                        newurl.save()
                        return redirect(shortner)
                    elif counter <= 50:
                        print("Not P hello bangladesh how are you")
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
            expire_date = check.expire_date
            now = datetime.now()
            expire_date = expire_date.strftime("%Y/%m/d %H:%M:%S")
            now = now.strftime("%Y/%m/d %H:%M:%S")
            if expire_date >= now:
                print("Basssssssssssssssssssssssss")
                check.visits = check.visits + 1
                check.save()
                url_to_redirect = check.original_url

                return redirect(url_to_redirect)
            else:
                return HttpResponse("<h1>Expired</h1>")

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
