from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post,Comment,Profile

class RegisterForm(UserCreationForm):
    email=forms.EmailField(required=True,widget=forms.EmailInput(attrs={'placeholder':'Email address'}))
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        widgets={'username':forms.TextInput(attrs={'placeholder':'Username'})}
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['password1'].widget.attrs.update({'placeholder':'Password'})
        self.fields['password2'].widget.attrs.update({'placeholder':'Confirm password'})
        for field in self.fields.values():
            field.help_text=''

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['content','image','image_url']
        widgets={
            'content':forms.Textarea(attrs={'rows':3,'placeholder':'Write a caption...'}),
            'image':forms.ClearableFileInput(attrs={'accept':'image/*'}),
            'image_url':forms.URLInput(attrs={'placeholder':'Or paste an image URL (optional)'})
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['content']
        widgets={'content':forms.TextInput(attrs={'placeholder':'Add a comment...'})}

class ProfileForm(forms.ModelForm):
    first_name=forms.CharField(required=False,max_length=30)
    last_name=forms.CharField(required=False,max_length=30)
    email=forms.EmailField(required=True)
    class Meta:
        model=Profile
        fields=['bio','avatar_url','location']
