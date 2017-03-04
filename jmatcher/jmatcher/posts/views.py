from django.http import HttpResponse
from django.shortcuts import render
from .forms import PostForm
from .models import Post
from django.shortcuts import redirect

def home(request):
    return render(request, 'posts/home.html')


def post_status(request):
	if request.method == "POST":
		#calling the postform class and it is giving a dictionary and it validates
		form = PostForm(request.POST)
		if form.is_valid():
			post = Post(description=form.cleaned_data['description'], user=request.user)
			post.save()
			return redirect("posts:get_all_posts")
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
	posts = Post.objects.all()
	context['posts'] = posts
	return render(request, "posts/showAllPosts.html", context)

def get_post(request, post_id):
	context = {}
	post_detail = Post.objects.get(pk=post_id)
	context['post_detail'] = post_detail
	return render(request, "posts/showPost.html", context)
