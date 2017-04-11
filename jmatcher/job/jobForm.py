from django import forms
from django.forms import Textarea

from .models import Job

class jobForm(forms.ModelForm):
	skill = forms.CharField()
	location = forms.CharField()

	class Meta:
		model = Job
		fields = ('post_name','employment_type', 'industry', 'experience', 'description', )
		widgets = {
		'description': Textarea(attrs={'cols': 80, 'rows': 20}),
		}