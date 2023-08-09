from django import forms
from django.contrib.auth.forms import AuthenticationForm

from kickbox_academy.core.models import CustomUser


class UserProfileForm(forms.ModelForm):
    password_confirmation = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirmation = cleaned_data.get('password_confirmation')

        if password and password_confirmation and password != password_confirmation:
            raise forms.ValidationError("Passwords do not match.")


class UserLoginForm(AuthenticationForm):
    pass
