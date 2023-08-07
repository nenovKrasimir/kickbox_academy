from django import forms

from kickbox_academy.core.models import CustomUser


class UserProfileForm(forms.ModelForm):
    class Meta:
            model = CustomUser
            fields = ['email', 'first_name', 'last_name']
