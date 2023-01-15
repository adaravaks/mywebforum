from django.shortcuts import render, redirect
from .models import Post, User, Theme
from .forms import PostForm, NewUserForm, ThemeForm


def home(request):
    context = {
        'title': 'Начало'
    }
    return render(request, 'main/home.html', context)


def index(request):
    themes = Theme.objects.order_by('-id')
    context = {'title': 'Главная страница', 'themes': themes}
    return render(request, 'main/index.html', context)


def about(request):
    return render(request, 'main/about-us.html')


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


def theme(request, theme_id):
    theme_from_main = Theme.objects.filter(pk=theme_id)
    posts_related = Post.objects.filter(parent_theme_id=theme_id)
    error = ''
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        parent_theme = Theme.objects.get(pk=theme_id)
        form.instance.parent_theme = parent_theme
        if form.is_valid():
            form.save()
            return redirect(parent_theme)
        else:
            error = 'Неверный ввод'

    form = PostForm()
    context = {
        'theme_id': theme_id,
        'theme_from_main': theme_from_main,
        'posts_related': posts_related,
        'error': error,
        'form': form
    }
    return render(request, 'main/theme.html', context)


def newtheme(request):
    error = ''
    if request.method == 'POST':
        form = ThemeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = 'Неверный ввод'

    form = ThemeForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/new-theme.html', context)

# TODO: Reformat functions names to camelCase later
# TODO: Change some of the view functions to view classes
