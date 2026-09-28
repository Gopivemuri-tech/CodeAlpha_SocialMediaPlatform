from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import get_object_or_404,redirect,render
from django.views.decorators.http import require_POST
from .forms import RegisterForm,PostForm,CommentForm,ProfileForm
from .models import Post,Like,Comment,Follow,Profile

def register(request):
    if request.user.is_authenticated: return redirect('feed')
    form=RegisterForm(request.POST or None)
    if request.method=='POST' and form.is_valid():
        user=form.save(); login(request,user); messages.success(request,'Welcome! Your account is ready.'); return redirect('feed')
    return render(request,'registration/register.html',{'form':form})

@login_required
def feed(request):
    posts=Post.objects.select_related('author','author__profile').prefetch_related('likes','comments__author')
    liked=set(Like.objects.filter(user=request.user,post__in=posts).values_list('post_id',flat=True))
    following_ids=list(Follow.objects.filter(follower=request.user).values_list('following_id',flat=True))
    suggested=User.objects.exclude(id=request.user.id).exclude(id__in=following_ids)[:5]
    return render(request,'social/feed.html',{'posts':posts,'post_form':PostForm(),'comment_form':CommentForm(),'liked':liked,'suggested':suggested})

@login_required
@require_POST
def create_post(request):
    form=PostForm(request.POST,request.FILES)
    if form.is_valid():
        p=form.save(commit=False); p.author=request.user; p.save(); messages.success(request,'Post published.')
    return redirect('feed')

@login_required
@require_POST
def delete_post(request,pk):
    p=get_object_or_404(Post,pk=pk,author=request.user); p.delete(); messages.success(request,'Post deleted.'); return redirect(request.POST.get('next') or 'feed')

@login_required
@require_POST
def toggle_like(request,pk):
    p=get_object_or_404(Post,pk=pk); obj,created=Like.objects.get_or_create(user=request.user,post=p)
    if not created: obj.delete()
    return redirect(request.POST.get('next') or 'feed')

@login_required
@require_POST
def add_comment(request,pk):
    p=get_object_or_404(Post,pk=pk); form=CommentForm(request.POST)
    if form.is_valid():
        c=form.save(commit=False); c.post=p; c.author=request.user; c.save()
    return redirect(request.POST.get('next') or 'feed')

@login_required
def profile_view(request,username):
    user=get_object_or_404(User,username=username); profile,_=Profile.objects.get_or_create(user=user)
    posts=user.posts.prefetch_related('likes','comments__author')
    is_following=Follow.objects.filter(follower=request.user,following=user).exists() if user!=request.user else False
    liked=set(Like.objects.filter(user=request.user,post__in=posts).values_list('post_id',flat=True))
    return render(request,'social/profile.html',{'profile_user':user,'profile':profile,'posts':posts,'is_following':is_following,'liked':liked,'comment_form':CommentForm(),'followers_count':user.follower_relations.count(),'following_count':user.following_relations.count()})

@login_required
@require_POST
def toggle_follow(request,username):
    target=get_object_or_404(User,username=username)
    if target==request.user: return redirect('profile',username=username)
    rel,created=Follow.objects.get_or_create(follower=request.user,following=target)
    if not created: rel.delete()
    return redirect('profile',username=username)

@login_required
def edit_profile(request):
    profile,_=Profile.objects.get_or_create(user=request.user)
    if request.method=='POST':
        form=ProfileForm(request.POST,instance=profile)
        if form.is_valid():
            obj=form.save(); request.user.first_name=form.cleaned_data['first_name']; request.user.last_name=form.cleaned_data['last_name']; request.user.email=form.cleaned_data['email']; request.user.save(); messages.success(request,'Profile updated.'); return redirect('profile',username=request.user.username)
    else:
        form=ProfileForm(instance=profile,initial={'first_name':request.user.first_name,'last_name':request.user.last_name,'email':request.user.email})
    return render(request,'social/edit_profile.html',{'form':form})

@login_required
def explore(request):
    posts=Post.objects.select_related('author','author__profile').prefetch_related('likes','comments').order_by('-created_at')
    return render(request,'social/explore.html',{'posts':posts})

@login_required
def search_users(request):
    q=request.GET.get('q','').strip(); users=User.objects.none()
    if q: users=User.objects.filter(Q(username__icontains=q)|Q(first_name__icontains=q)|Q(last_name__icontains=q)).select_related('profile')[:20]
    return render(request,'social/search.html',{'q':q,'users':users})
