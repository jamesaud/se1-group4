from django import forms
from .models import Employer
from jmatcher.users.models import User
from django.utils.translation import ugettext_lazy as _

class EmployerForm(forms.ModelForm):
    description = forms.CharField( widget=forms.Textarea )

    class Meta:
        model = Employer
        fields = ['company_name', 'website', 'size', 'description']


class EmployerUserForm(forms.ModelForm):
    class Meta:
        model = User

        fields = ['short_description', 'image',  'background']
