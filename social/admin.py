from django.contrib import admin
from .models import Profile,Follow,Post,Like,Comment
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin): list_display=('user','location','created_at'); search_fields=('user__username','bio')
@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin): list_display=('follower','following','created_at')
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=('author','short_content','created_at')
    search_fields=('author__username','content')
    def short_content(self,obj): return obj.content[:50]
class LikeAdmin(admin.ModelAdmin): list_display=('user','post','created_at')
admin.site.register(Like,LikeAdmin)
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin): list_display=('author','post','created_at')
