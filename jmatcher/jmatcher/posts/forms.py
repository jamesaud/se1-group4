from django import forms

from .models import Post
from .models import PostComments

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['description']

class CommentForm(forms.ModelForm):
	class Meta:
		model = PostComments
		fields = ['comment']