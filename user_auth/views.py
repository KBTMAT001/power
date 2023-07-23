from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse



# Create your views here.
def user_login(request):
    """
    Renders the user login html upon a login request.
    """

    return render(request, 'authentication/login.html')

def authenticate_user(request):
    """
    Handles user authentication and renders the appropriate html.

    :param username: input into the username field
    :type username: string
    :param password: input into the password field
    :type password: string
    :param user: boolean for user authenticate
    :type user: boolean
    :return: Relevan html file path
    :rtype:str
    """
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)

    if user is None:
        return render(request,'authentication/login_fail.html')
    else:
        login(request, user)
        return HttpResponseRedirect(reverse('user_auth:show_user'))
    
def show_user(request):
    """
    View to return user details shoudl login be succesful
    """
    print(request.user.username)
    return render(request, 'authentication/user.html', {
        "username": request.user.username,
        "password": request.user.password
    })