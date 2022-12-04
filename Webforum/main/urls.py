from django.urls import path
from . import views

urlpatterns = [
    path('main', views.index, name='index'),
    path('about-us', views.about, name='about-us'),
    path('new-post', views.newpost, name='new-post'),
    path('', views.home, name='home'),
]