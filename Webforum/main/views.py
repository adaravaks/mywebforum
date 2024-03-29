from django.contrib.auth import logout, login, get_user_model, get_user
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib import messages
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_str, force_bytes
from django.core.mail import EmailMessage

from .models import Post, User, Theme
from .forms import PostForm, ThemeForm, RegisterUserForm, LoginUserForm
from .tokens import account_activation_token
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
    main_theme = Theme.objects.get(pk=theme_id)
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
        'main_theme': main_theme,
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


def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Зареган. Логинься.', extra_tags='alert-success alert')
        return redirect('/accounts/login')
    else:
        messages.error(request, 'Что-то наебнулось', extra_tags='alert-danger alert')
    return redirect('index')


def activateEmail(request, user, to_email):
    mail_subject = 'Подтверждение электронной почты'
    message = render_to_string('main/email-verification-message.html', {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        'protocol': 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, f'Ах ты ёбаный {user}, быстро пиздуй на свой {to_email} и подтверждай свою поганую регистрацию.', extra_tags='alert-success alert')
    else:
        messages.error(request, f'Хуй тебе, а не письмо на {to_email}', extra_tags='alert-danger alert')


class RegisterUser(CreateView, DataMixin):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        activateEmail(self.request, user, form.cleaned_data.get('email'))
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


def profile(request, username):
    wanted_user = User.objects.get(username=username)
    context = {}
    if request.user.is_authenticated:  # TODO: The fuck is this? I neither remember coding that nor want my website to behave that way
        context['user'] = wanted_user
    return render(request, 'main/profile.html', context)
