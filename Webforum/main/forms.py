from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Post, Theme
from django.forms import ModelForm, TextInput, Textarea, FileInput, PasswordInput, CharField, EmailInput, EmailField
from captcha.fields import CaptchaField, CaptchaTextInput


class PostForm(ModelForm):
    captcha = CaptchaField(label='Капча', widget=CaptchaTextInput(attrs={'placeholder': 'Капча'}))
    class Meta:
        model = Post
        fields = ('theme', 'text', 'post_picture')
        widgets = {
            'theme': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Тема поста'}),

            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Сам пост'}),

            'post_picture':  FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Вложение поста'})
        }


class ThemeForm(ModelForm):
    captcha = CaptchaField(label='Капча', widget=CaptchaTextInput(attrs={'placeholder': 'Капча'}))
    class Meta:
        model = Theme
        fields = ('header', 'text', 'media')
        widgets = {
            'header': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Заголовок темы'}),

            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст темы'}),

            'media': FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Вложение к теме'})
        }


class RegisterUserForm(UserCreationForm):
    username = CharField(label='Имя пользователя', widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя пользователя'}))
    email = EmailField(label='Адрес электронной почты', widget=EmailInput(attrs={'class': 'form-control', 'placeholder': 'Адрес электронной почты'}))
    password1 = CharField(label='Пароль', widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}))
    password2 = CharField(label='Пароль ещё раз', widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль ещё раз'}))
    captcha = CaptchaField(label='Капча', widget=CaptchaTextInput(attrs={'placeholder': 'Капча'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя пользователя'}),

            'email': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Адрес электронной почты'}),

            'password1': PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пароль'}),

            'password2': PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пароль ещё раз'})
        }


class LoginUserForm(AuthenticationForm):
    username = CharField(label='Имя пользователя', widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя пользователя'}))
    password = CharField(label='Пароль', widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}))
    captcha = CaptchaField(label='Капча', widget=CaptchaTextInput(attrs={'placeholder': 'Капча'}))
