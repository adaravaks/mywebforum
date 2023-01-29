from django.urls import path, include
from . import views

urlpatterns = [
    path('main', views.index, name='index'),
    path('about-us', views.about, name='about-us'),
    path('', views.home, name='home'),
    path('theme/<int:theme_id>', views.theme, name='theme'),
    path('new-theme', views.newtheme, name='new-theme'),
    path('accounts/register', views.RegisterUser.as_view(), name='accounts/register'),
    path('accounts/login', views.LoginUser.as_view(), name='accounts/login'),
    path('accounts/logout', views.logout_user, name='accounts/logout'),
    path('captcha/', include('captcha.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
    path('verification/', include('verify_email.urls')),
]