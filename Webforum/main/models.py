from django.db import models
from django.db.models import SET_NULL, PROTECT
from django.urls import reverse


class Post(models.Model):
    theme = models.CharField('Тема', max_length=70)
    text = models.TextField('Пост')
    post_picture = models.ImageField(upload_to='communication_pictures/posts/%Y/%m/%d/')
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    parent_theme = models.ForeignKey('Theme', on_delete=PROTECT)
    # author = models.ForeignKey('User', on_delete=PROTECT, null=True)  # TODO: Once authorisation is created, uncomment this and make sure it works

    def __str__(self):
        return self.theme

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def get_absolute_url(self):
        return reverse('theme', kwargs={'theme_id': self.pk})


class User(models.Model):
    username = models.CharField(max_length=30)
    about_user = models.TextField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pictures/%Y/%m/%d/')
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def get_absolute_url(self):
        return reverse('theme', kwargs={'theme_id': self.pk})


class Theme(models.Model):
    header = models.CharField(max_length=100, db_index=True)
    media = models.ImageField(upload_to='communication_pictures/themes/%Y/%m/%d/')
    text = models.TextField(max_length=500)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    # author = models.ForeignKey('User', on_delete=PROTECT, null=True)  # TODO: Once authorisation is created, uncomment this and make sure it works

    def __str__(self):
        return self.header

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'

    def get_absolute_url(self):
        return reverse('theme', kwargs={'theme_id': self.pk})
