from django.contrib import admin
from .models import Profile, Post,LikePost, FolowersCount

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass

@admin.register(LikePost)
class LikePostAdmin(admin.ModelAdmin):
    pass

@admin.register(FolowersCount)
class FollowersCountAdmin(admin.ModelAdmin):
    pass
# admin.site.register(Profile)