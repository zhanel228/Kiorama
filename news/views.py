from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import DoramaNewsForm, UserRegisterForm, DoramaVideoForm 


from .models import DoramaNews, DoramaVideo, Comment


def news_list(request):
    news = DoramaNews.objects.all().order_by('-created_at')
    query = request.GET.get('q')
    if query:
        news = news.filter(dorama_name__icontains=query)

    context = {
        'news': news,
        'query': query,
    }
    return render(request, 'news/news_list.html', context)


def news_detail(request, id):
    news_item = get_object_or_404(DoramaNews, id=id)
    

    if request.method == 'POST' and request.user.is_authenticated:
        body = request.POST.get('body')
        if body:
            Comment.objects.create(
                post=news_item, 
                author=request.user, 
                body=body
            )
            return redirect('news_detail', id=id)

    return render(request, 'news/news_detail.html', {'news': news_item})


@login_required
def like_view(request, id):
    post = get_object_or_404(DoramaNews, id=id)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    
    return HttpResponseRedirect(reverse('news_detail', args=[str(id)]))


@login_required(login_url='register')  
def add_news(request):
    if request.method == 'POST':
        form = DoramaNewsForm(request.POST, request.FILES)
        if form.is_valid():
            news = form.save(commit=False)
            news.author = request.user  
            news.save()
            return redirect('news_list')
    else:
        form = DoramaNewsForm()
    return render(request, 'news/add_news.html', {'form': form})


def video_list(request):
    videos = DoramaVideo.objects.all().order_by('-id') 
    return render(request, 'news/video_list.html', {'videos': videos})


@login_required
def add_video(request):
    if request.method == 'POST':
        form = DoramaVideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('reelse') 
    else:
        form = DoramaVideoForm()
    return render(request, 'news/add_video.html', {'form': form})


@login_required
def profile_view(request):
    my_news = DoramaNews.objects.filter(author=request.user).order_by('-created_at')
    return render(request, 'news/profile.html', {
        'my_news': my_news
    })


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('news_list')
    else:
        form = UserRegisterForm()
    return render(request, 'news/register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('news_list')