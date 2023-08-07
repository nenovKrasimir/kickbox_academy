from django.shortcuts import render, redirect


# Create your views here.


def home_page(request):
    return render(request, template_name='index.html')


def join_us_page(request):
    return render(request=request, template_name='join_us.html', context=context)


def login_page(request):
    pass
