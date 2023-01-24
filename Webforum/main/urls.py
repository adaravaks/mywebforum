from django.urls import path
from . import views

urlpatterns = [
    path('main', views.index, name='index'),
    path('about-us', views.about, name='about-us'),
    path('', views.home, name='home'),
    #path('new-user', views.newuser, name='new-user'),
    #path('users', views.users, name='users'),
    path('theme/<int:theme_id>', views.theme, name='theme'),
    path('new-theme', views.newtheme, name='new-theme'),
    path('register', views.RegisterUser.as_view(), name='register'),
    path('login', views.LoginUser.as_view(), name='login'),
    path('logout', views.logout_user, name='logout')
]