from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm


def home(request):
    context = {
        'title': 'Начало'
    }
    return render(request, 'main/home.html', context)


def index(request):
    posts = Post.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Главная страница', 'posts': posts})


def about(request):
    return render(request, 'main/about-us.html')


def newpost(request):
    error = ''
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = 'Неверный формат поста'

    form = PostForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/new-post.html', context)

