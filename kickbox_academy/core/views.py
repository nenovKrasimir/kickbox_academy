from django.shortcuts import render, redirect

from kickbox_academy.core.forms import UserProfileForm, UserLoginForm


# Create your views here.


def home_page(request):
    return render(request, template_name='index.html')


def join_us_page(request):
    return render(request=request, template_name='join_us.html')


def login_page(request):
    context = {'form': UserLoginForm}
    return render(request=request, template_name='login.html', context=context)
