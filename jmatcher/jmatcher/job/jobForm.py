from django import forms

from .models import Job

class jobForm(forms.ModelForm):

    class Meta:
        model = Job
        fields = ('post_name','employment_type', 'industry','location', 'experience', 'description')
