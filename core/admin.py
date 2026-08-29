from django.contrib.admin import ModelAdmin as BaseModelAdmin
from django.contrib import admin
from django.utils.translation import gettext as _

from .models import *

class UserModelAdmin(BaseModelAdmin):
    ordering = ['id']
    list_display = ['email', 'f_name', 'l_name']
    #divide into sections
    fieldsets = (
        (_('Login Information'), {'fields': ('email', 'password')}),
        (_('Personal Information'), {'fields': ('f_name', 'l_name', 'phone_number')}),
        (_('Permissions'), {'fields': ('is_staff', 'is_active', 'is_superuser')}),
        (_('Dates'), {'fields': ('birth_date', 'last_login')}),
    )
# Register your models here.
admin.site.register(User, UserModelAdmin)
admin.site.register(Hotel)
admin.site.register(Room)
admin.site.register(Reservation)
