from django.db import models
from django.db.models import SET_NULL, PROTECT, CASCADE
from django.urls import reverse
from django.contrib.auth.models import User  # This is NOT unused import. Do not delete this


class Post(models.Model):
    theme = models.CharField('Тема', max_length=70)  # TODO: delete.
    text = models.TextField('Пост', max_length=3000)
    post_picture = models.ImageField(upload_to='communication_pictures/posts/%Y/%m/%d/', blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    parent_theme = models.ForeignKey('Theme', on_delete=CASCADE, blank=True)
    author = models.ForeignKey('auth.User', to_field='username', on_delete=PROTECT, null=True)

    def __str__(self):
        return self.theme

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})


class Theme(models.Model):
    header = models.TextField(max_length=500, db_index=True)
    media = models.ImageField(upload_to='communication_pictures/themes/%Y/%m/%d/', blank=True)
    text = models.TextField(max_length=5000)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey('auth.User', to_field='username', on_delete=PROTECT, null=True)

    def __str__(self):
        return self.header

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'

    def get_absolute_url(self):
        return reverse('theme', kwargs={'theme_id': self.pk})
