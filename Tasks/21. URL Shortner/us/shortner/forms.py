from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.db import models


class CreateCustomUser(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['account_type']


class CreateUserForm(UserCreationForm):
    account_type = models.BooleanField(default=False, blank=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1',
                  'password2']
