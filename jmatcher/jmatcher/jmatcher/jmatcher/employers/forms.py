from django import forms
from .models import Employer
from django.utils.translation import ugettext_lazy as _

class EmployerForm(forms.ModelForm):
    class Meta:
        model = Employer
        fields = ['company_name', 'website', 'size', 'description', ]
