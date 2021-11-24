from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Diary, FriendsApply, User
# Register your models here.

admin.site.register(Diary)
admin.site.register(User, UserAdmin)
admin.site.register(FriendsApply)
UserAdmin.fieldsets += (("Custom fields", {"fields": ("nickname", "friends")}),)
