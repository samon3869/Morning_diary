from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Diary, User
# Register your models here.

admin.site.register(Diary)
admin.site.register(User, UserAdmin)