from django.http import HttpResponse
from django.shortcuts import render
from .forms import PostForm, CommentForm
from .models import Post, PostComments

def home(request):
    return render(request, 'posts/home.html')


def post_status(request):
	if request.method == "POST":
		#calling the postform class and it is giving a dictionary and it validates
		form = PostForm(request.POST)
		if form.is_valid():
			post = Post(description=form.cleaned_data['description'], user=request.user)
			post.save()
			return render(request, 'posts/home.html')
		else:
			return HttpResponse("There is an error")
	else:		
		form = PostForm()
		context = {
		"form": form,
		}
		return render(request, "posts/postStatus.html", context)

def get_all_posts(request):
	user = request.user
	context = {}
	posts = user.post_set.all()
	context['posts'] = posts
	return render(request, "posts/showAllPosts.html", context)

def get_post(request, post_id):
	if request.method == "POST":
		comment_form = CommentForm(request.POST)
		if comment_form.is_valid():
			post = Post.objects.get(pk=post_id)
			comment = PostComments(commenting_user=request.user, post=post, comment=comment_form.cleaned_data['comment'])
			comment.save()
	context = {}
	comment_form = CommentForm()
	post_detail = Post.objects.get(pk=post_id)
	context['post_detail'] = post_detail
	context['comment_form'] = comment_form
	return render(request, "posts/showPost.html", context)

from django.http import JsonResponse
from django.forms.models import model_to_dict

def post_comments(request, post_id):
	if request.method == "POST":
		comment_form = CommentForm(request.POST)
		if comment_form.is_valid():
			post = Post.objects.get(pk=post_id)
			comment = PostComments(commenting_user=request.user, post=post, comment=comment_form.cleaned_data['comment'])
			comment.save()



