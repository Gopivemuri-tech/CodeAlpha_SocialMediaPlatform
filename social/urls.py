from django.urls import path
from . import views
urlpatterns=[
path('',views.feed,name='feed'),path('explore/',views.explore,name='explore'),path('register/',views.register,name='register'),path('post/create/',views.create_post,name='create_post'),path('post/<int:pk>/delete/',views.delete_post,name='delete_post'),path('post/<int:pk>/like/',views.toggle_like,name='toggle_like'),path('post/<int:pk>/comment/',views.add_comment,name='add_comment'),path('profile/edit/',views.edit_profile,name='edit_profile'),path('u/<str:username>/',views.profile_view,name='profile'),path('u/<str:username>/follow/',views.toggle_follow,name='toggle_follow'),path('search/',views.search_users,name='search_users')]
