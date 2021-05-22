from django.contrib import admin
from .models import *


class AdminShortUrl(admin.ModelAdmin):
    list_display = ('original_url', 'short_query',
                    'date', 'user', 'expire_date')


class AdminCustomUser(admin.ModelAdmin):
    list_display = ('account_type', )


# Register your models here.


admin.site.register(ShortUrl, AdminShortUrl)
admin.site.register(CustomUser, AdminCustomUser)
