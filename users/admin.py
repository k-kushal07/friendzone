from django.contrib import admin
from .models import Profile, FriendRequest
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Profile._meta.fields]

class FriendRequestAdmin(admin.ModelAdmin):
    list_display = [field.name for field in FriendRequest._meta.fields]

   
admin.site.register(Profile, ProfileAdmin)
admin.site.register(FriendRequest, FriendRequestAdmin)