from django import forms
from django.forms import Textarea

from .models import Job, JobApplication

class jobApplicationForm(forms.ModelForm):
	class Meta:
		model = JobApplication
		fields = ('attachment',)
		labels = {
		'attachment': 'Resume/Cover Letter',
		}

class jobForm(forms.ModelForm):
	skill = forms.CharField()
	location = forms.CharField()

	def clean(self):
		cleaned_data = super(jobForm, self).clean()
		education_weightage = cleaned_data.get("education_weightage")
		experience_weightage = cleaned_data.get("experience_weightage")
		skills_weightage = cleaned_data.get("skills_weightage")

		if(education_weightage+experience_weightage+skills_weightage!=100):
			raise forms.ValidationError("All the weightage should sum up to 100")

	class Meta:
		model = Job
		fields = ('post_name','employment_type', 'industry', 'experience', 'description', 'education_weightage', 'experience_weightage', 'skills_weightage')
		labels = {
			'post_name': "Job Title",
		}
		widgets = {
		'description': Textarea(attrs={'cols': 80, 'rows': 20}),
		}