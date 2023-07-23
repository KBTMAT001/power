from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import RegistrationForm


# Create your views here.
def register_home(request):
    return render(request, 'authentication/register.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'registration/register_success.html')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})
    
def show_user(request):
    print(request.user.username)
    return render(request, 'authentication/user.html', {
        "username": request.user.username,
        "password": request.user.password
    })
