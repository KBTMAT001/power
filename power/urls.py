from django.urls import path, include
from django.views.generic import ListView, DetailView
from . import views

app_name = 'power'
urlpatterns = [
    path('', views.home, name='home'),
    path('input/', views.input, name='input'),
    path('backend/', views.backend, name='backend'),
    path('logout/',views.log_out, name='log_out'),
    path('enquiry/',views.enquiry,name = 'enquiry'),
    path('submit/',views.submit,name = 'submit'),
    path('overview/',views.overview,name = 'overview'),
    path('mtest/',views.mtest,name ='mtest')
    
]