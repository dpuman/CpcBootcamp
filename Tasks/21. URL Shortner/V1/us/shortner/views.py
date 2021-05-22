from django.shortcuts import redirect, render
from .models import *
from .forms import UrlForm
from .shortner import Shortner
# Create your views here.


def home(request, token):
    long_url = ShortUrls.objects.filter(short_url=token)[0]

    return redirect(long_url.long_url)


def shortner(request):
    form = UrlForm(request.POST)
    a = ""
    if request.method == 'POST':
        if form.is_valid():
            new_form = form.save(commit=False)
            a = Shortner().issue_token()
            new_form.short_url = a
            new_form.save()
        else:
            form = UrlForm()
            a = "Invalid URL"

    context = {
        'form': form,
        'a': a,
    }
    return render(request, 'shortner/index.html', context)
