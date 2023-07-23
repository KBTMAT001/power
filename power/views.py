from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.urls import path,reverse
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth import logout
from .models import Enquiry
from datetime import datetime
# Create your views here.



def home(request):
    return render(request, 'home.html')


def input(request):
    if request.user.is_authenticated:
        return render(request,'calculation/input.html')
    else:
        return render(request,'authentication/login_need.html')


def backend(request):
    company_in = request.POST['company']
    profile_in = request.POST['profile']
    demand_in = int(request.POST['demand'])

    if profile_in == "residential":
        saving = demand_in*5
    elif profile_in == "industrial":
        saving = demand_in*10
    else:
        saving = demand_in*100

    return render(request,'calculation/backend.html',{"saving":saving,"profile":profile_in,"demand":demand_in,"company":company_in})
    
def log_out(request):
    logout(request)
    return render(request, 'authentication/logout.html')

def enquiry(request):
    return render(request,'enquiry.html')

def submit(request):
    company_in = request.POST['company']
    person_in = request.POST['person']
    email_in = request.POST['email']
    
    Enquiry.objects.create(company = company_in,date_sent = datetime.today(),person = person_in,email = email_in)

    return render(request,'confirmation.html',{"company":company_in,"person":person_in,"email":email_in})

def overview(request):
    if request.user.is_staff:
        latest_enquiry_list = Enquiry.objects.order_by('-date_sent')[:5]
        context ={'latest_enquiry_list':latest_enquiry_list}
        return render(request,'overview.html',context)
    else:
        return render(request,'authentication/login_need_admin.html')

def mtest(request):
    return render(request,'registration/register_success.html')

    