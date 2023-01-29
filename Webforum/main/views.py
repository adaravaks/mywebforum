from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import Post, User, Theme
from .forms import PostForm, ThemeForm, RegisterUserForm, LoginUserForm
from .utils import DataMixin


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


def theme(request, theme_id):
    theme_from_main = Theme.objects.filter(pk=theme_id)  # TODO: Change 'filter' to 'get' and deal with that for-loop in theme.html
    posts_related = Post.objects.filter(parent_theme_id=theme_id)
    error = ''
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        parent_theme = Theme.objects.get(pk=theme_id)
        author = User.objects.get(pk=request.user.id)
        form.instance.parent_theme = parent_theme
        form.instance.author = author
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
        author = User.objects.get(pk=request.user.id)
        form.instance.author = author
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


class RegisterUser(CreateView, DataMixin):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('index')


def logout_user(request):
    logout(request)
    return redirect('index')


# TODO: Change some of the view functions to view classes
