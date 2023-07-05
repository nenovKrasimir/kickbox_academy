from django.shortcuts import render, redirect

from kickbox_academy.core.forms import CreateUserForm


# Create your views here.


def home_page(request):
    return render(request, template_name='index.html')


def register_page(request):
    form = CreateUserForm
    context = {'form': form}

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login-page')

    return render(request=request, template_name='join_us.html', context=context)


