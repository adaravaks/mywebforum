from .models import Post
from django.forms import ModelForm, TextInput, Textarea


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['theme', 'text']
        widgets = {'theme': TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Тема поста'
        }),
            'text': Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Сам пост'})
        }

