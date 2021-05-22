from django.contrib import admin
from .models import *


class ShortUrlsAdmin(admin.ModelAdmin):

    list_display = ('short_url', 'long_url')


# Register your models here.
admin.site.register(ShortUrls, ShortUrlsAdmin)
