from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from kickbox_academy.core.forms import UserProfileForm, UserLoginForm


# Create your views here.


def home_page(request):
    return render(request, template_name='index.html')


def join_us_page(request):
    return render(request=request, template_name='join_us.html')


class CustomLoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('home')


def registration_page(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('home_page')

    else:
        form = UserProfileForm()

    return render(request, 'register.html', {'form': form})
