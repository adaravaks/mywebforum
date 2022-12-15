from django.shortcuts import render, redirect
from .models import Post, User
from .forms import PostForm, NewUserForm


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
        form = PostForm(request.POST)  # PostForm - мой класс, не джанговский. Не путать!
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
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
        else:
            error = 'Ищи ошибку мудак'

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
