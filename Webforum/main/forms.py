from .models import Post, User
from django.forms import ModelForm, TextInput, Textarea, FileInput


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['theme', 'text']
        widgets = {
            'theme': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Тема поста'}),

            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Сам пост'})
        }


class NewUserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'about_user']  # 'profile_pic']
        widgets = {
            'username': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Юзернейм пользователя'}),

            'about_user': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'О пользователе'}),

            # 'profile_pic': FileInput(attrs={
            #    'class': 'form-control'}),
        }


