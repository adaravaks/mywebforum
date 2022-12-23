from django.shortcuts import render, redirect
from .models import Post, User
from .forms import PostForm, NewUserForm, ThemeForm


def home(request):
    context = {
        'title': 'Начало'
    }
    return render(request, 'main/home.html', context)


def index(request):
    posts = Post.objects.order_by('-id')
    context = {'title': 'Главная страница', 'posts': posts}
    return render(request, 'main/index.html', context)


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


def newuser(request):
    error = ''
    if request.method == 'POST':
        form = NewUserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('users')
        else:
            error = 'Неверный ввод'

    form = NewUserForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/new-user.html', context)


def users(request):
    users = User.objects.order_by('create_time')
    context = {
        'users': users,
    }
    return render(request, 'main/users.html', context)


def theme(request):
    return render(request, 'main/theme.html')


def newtheme(request):
    error = ''
    if request.method == 'POST':
        form = ThemeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('theme')
        else:
            error = 'Неверный ввод'

    form = ThemeForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/new-theme.html', context)

# Reformat functions names to camelCase later
