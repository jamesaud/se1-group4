from django import forms
from .models import User
from django.utils.translation import ugettext_lazy as _

class UserSignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'image']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'image', 'short_description', 'background']
