from django import forms
from django.contrib.auth.forms import AuthenticationForm

from kickbox_academy.core.models import CustomUser


class UserProfileForm(forms.ModelForm):
    class Meta:
            model = CustomUser
            fields = ['email', 'first_name', 'last_name']


class UserLoginForm(AuthenticationForm):
    pass