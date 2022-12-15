from django.db import models


class Post(models.Model):
    theme = models.CharField('Тема', max_length=70)
    text = models.TextField('Пост')

    def __str__(self):
        return self.theme

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'


class User(models.Model):
    username = models.CharField(max_length=30)
    about_user = models.TextField(blank=True)
    profile_pic = models.ImageField(upload_to='static/main/media/profile_pictures/%Y%m%d/')
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
