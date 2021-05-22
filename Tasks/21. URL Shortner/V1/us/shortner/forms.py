from django.forms import ModelForm
from .models import *


class UrlForm(ModelForm):
    class Meta:
        model = ShortUrls
        fields = ['long_url']
