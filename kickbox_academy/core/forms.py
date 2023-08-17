from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from kickbox_academy.core.models import CustomUser


class UserProfileForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class UserLoginForm(AuthenticationForm):
    pass
