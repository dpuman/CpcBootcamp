from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.models import User

# Create your models here.


class CustomUser(models.Model):
    my_user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_type = models.BooleanField(default=False, blank=True)


date = datetime.today() + timedelta(days=30)


class ShortUrl(models.Model):

    original_url = models.URLField(blank=False)
    short_query = models.CharField(blank=False, max_length=8)
    visits = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now, blank=True)
    expire_date = models.DateTimeField(default='', blank=True, null=True)
