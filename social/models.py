from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    bio=models.CharField(max_length=200,blank=True)
    avatar_url=models.URLField(blank=True)
    location=models.CharField(max_length=100,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.user.username

class Follow(models.Model):
    follower=models.ForeignKey(User,on_delete=models.CASCADE,related_name='following_relations')
    following=models.ForeignKey(User,on_delete=models.CASCADE,related_name='follower_relations')
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta:
        constraints=[models.UniqueConstraint(fields=['follower','following'],name='unique_follow')]
    def __str__(self): return f'{self.follower} -> {self.following}'

class Post(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts')
    content=models.TextField(max_length=1000)
    image=models.FileField(upload_to='posts/',blank=True,validators=[FileExtensionValidator(['jpg','jpeg','png','webp','gif'])])
    image_url=models.URLField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    class Meta: ordering=['-created_at']
    def __str__(self): return f'{self.author}: {self.content[:40]}'
    @property
    def like_count(self): return self.likes.count()

class Like(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='likes')
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='likes')
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta:
        constraints=[models.UniqueConstraint(fields=['user','post'],name='unique_like')]

class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='comments')
    content=models.CharField(max_length=500)
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta: ordering=['created_at']
    def __str__(self): return f'{self.author}: {self.content[:30]}'
