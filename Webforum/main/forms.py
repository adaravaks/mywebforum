from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Post, User as myUser, Theme
from django.forms import ModelForm, TextInput, Textarea, FileInput, PasswordInput, CharField, EmailInput, EmailField


class PostForm(ModelForm):
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


class NewUserForm(ModelForm):
    class Meta:
        model = myUser
        fields = ('username', 'about_user', 'profile_pic')
        widgets = {
            'username': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Юзернейм пользователя'}),

            'about_user': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'О пользователе'}),

            'profile_pic': FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Аватарка пользователя'}),
        }


class ThemeForm(ModelForm):
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
                'placeholder': 'Вложение к теме'}),
        }


class RegisterUserForm(UserCreationForm):
    username = CharField(label='Имя пользователя', widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя пользователя'}))
    email = EmailField(label='Адрес электронной почты', widget=EmailInput(attrs={'class': 'form-control', 'placeholder': 'Адрес электронной почты'}))
    password1 = CharField(label='Пароль', widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}))
    password2 = CharField(label='Пароль ещё раз', widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль ещё раз'}))

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