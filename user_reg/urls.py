from django.urls import path, include
from django.views.generic import ListView, DetailView
from . import views

app_name = 'user_reg'
urlpatterns = [
    path('', views.register, name='register'),
    path('show_user/', views.show_user, name='show_user')
]