from django import forms

from .models import Post, PostComments

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['description']
		labels = {'description' : ''}

class CommentForm(forms.ModelForm):
	class Meta:
		model = PostComments
		fields = ['comment']