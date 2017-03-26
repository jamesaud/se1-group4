from django import forms
from .models import Student
from django.utils.translation import ugettext_lazy as _

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['skills']

