from django import forms
from .models import Student, WorkExperience, Education, Project
from django.forms.models import inlineformset_factory
from django.utils.translation import ugettext_lazy as _
import datetime
from django.conf import settings

from django import forms
from .models import Student
from django.utils.translation import ugettext_lazy as _

class StudentForm(forms.ModelForm):
	skill = forms.CharField()
	class Meta:
		model = Student
		fields = ['position']


class WorkForm(forms.ModelForm):
    start_date = forms.DateField(widget=forms.TextInput(attrs={'class':'date'}), input_formats=settings.DATE_INPUT_FORMATS)
    end_date = forms.DateField(widget=forms.TextInput(attrs={'class':'date'}), input_formats=settings.DATE_INPUT_FORMATS)
    description = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = WorkExperience
        fields = ['title', 'position', 'start_date', 'end_date', 'description']

    def clean(self):
        start_date = self.cleaned_data.get("start_date")
        end_date = self.cleaned_data.get("end_date")
        if end_date and start_date:
            if end_date < start_date:
                msg = u"End date should be greater than start date."
                self._errors["end_date"] = self.error_class([msg])



class EducationForm(forms.ModelForm):
    start_date = forms.DateField(widget=forms.TextInput(attrs={'class':'date'}), input_formats=settings.DATE_INPUT_FORMATS)
    end_date = forms.DateField(widget=forms.TextInput(attrs={'class':'date'}), input_formats=settings.DATE_INPUT_FORMATS)


    class Meta:
        model = Education
        fields = ['institution_name', 'level', 'start_date', 'end_date']


class ProjectForm(forms.ModelForm):
    start_date = forms.DateField(widget=forms.TextInput(attrs={'class':'date'}), input_formats=settings.DATE_INPUT_FORMATS)
    end_date = forms.DateField(widget=forms.TextInput(attrs={'class':'date'}), input_formats=settings.DATE_INPUT_FORMATS)
    description = forms.CharField(widget=forms.Textarea())
    class Meta:
        model = WorkExperience
        fields = ['title', 'start_date', 'end_date', 'description']


WorkInlineForm = inlineformset_factory(Student, WorkExperience, form=WorkForm, extra=2)
EducationInlineForm = inlineformset_factory(Student, Education, form=EducationForm, extra=1, min_num=1)
ProjectInlineForm = inlineformset_factory(Student, Project, form=ProjectForm, extra=1, min_num=1)

