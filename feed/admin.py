from django.contrib import admin
from .models import Post, Comments, Like
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Post._meta.fields]

class CommentsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Comments._meta.fields]

class LikeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Like._meta.fields]


admin.site.register(Post, PostAdmin)
admin.site.register(Comments, CommentsAdmin)
admin.site.register(Like, LikeAdmin)