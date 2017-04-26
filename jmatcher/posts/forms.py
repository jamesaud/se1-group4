from django import forms

from .models import Post, PostComments

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['description']
		labels = {'description' : ''}
		widgets = {
			'description': forms.Textarea(attrs={'cols': 80, 'rows': 2, 'placeholder': "What's on your mind?"}),
		}

class CommentForm(forms.ModelForm):
	class Meta:
		model = PostComments
		fields = ['comment']