from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .forms import PostForm, CommentForm
from .models import Post, PostComments
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


try:
    from django.utils import simplejson as json
except ImportError:
    import json


def home(request):
    return render(request, 'posts/home.html')


def post_status(request):
    if request.method == "POST":
        # calling the postform class and it is giving a dictionary and it validates
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
    connections = user.connections.all()
    posts = set()

    connection_q = Post.objects.all()

    if connections.exists():
        for connection in connections:
            for post in connection.likes.all():
                posts.add(post)
            for post in connection.shares.all():
                posts.add(post)
            for post in connection.post_set.all():
                posts.add(post)

            connection_q |= connection.likes.all() | connection.shares.all() | connection.post_set.all()

    for post in user.post_set.all():
        posts.add(post)

    context = {}


    # NEW
    form = PostForm(request.POST or None)
    if request.method == "POST":
        # calling the postform class and it is giving a dictionary and it validates
        if form.is_valid():
            post = Post(description=form.cleaned_data['description'], user=request.user)
            post.save()

    context.update({
        "form": form,
    })


    from django.db.models import Q
    posts = Post.objects.filter(Q(user__in=user.connections.all()) | Q(user=user)) | connection_q
    posts = posts.distinct().order_by('-created_at')

    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 10)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context['posts'] = posts

    return render(request, "posts/showAllPosts.html", context)


def is_user_post_liked(user, post):
    if post.likes.all().exists():
        if post.likes.filter(username=user.username).exists():
            return True
        else:
            return False
    else:
        return False


def is_user_post_shared(user, post):
    if post.shares.all().exists():
        if post.shares.filter(username=user.username).exists():
            return True
        else:
            return False
    else:
        return False


def get_post(request, post_id):
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            post = Post.objects.get(pk=post_id)
            comment = PostComments(commenting_user=request.user, post=post,
                                   comment=comment_form.cleaned_data['comment'])
            comment.save()
    context = {}
    comment_form = CommentForm()
    post = Post.objects.get(pk=post_id)
    context['post'] = post
    context['comment_form'] = comment_form

    if is_user_post_liked(request.user, post):
        context['like_action'] = "UnLike"
    else:
        context['like_action'] = 'Like'

    if is_user_post_shared(request.user, post):
        context['share_action'] = "Shared"
    else:
        context['share_action'] = "Share"

    return render(request, "posts/showPost.html", context)


def like_post(request):
    if request.method == "POST":
        post_id = request.POST.get("post_id")

        user = request.user
        post = Post.objects.get(pk=post_id)

        if is_user_post_liked(user, post):
            post.likes.remove(user)
            like_button_text = "Like"
        else:
            post.likes.add(user)
            like_button_text = "UnLike"

        post.save()
        print(post.likes.all())
        response = JsonResponse({'like_button_text': like_button_text})
        return response


def share_post(request):
    if request.method == "POST":
        post_id = request.POST.get("post_id")

        user = request.user
        post = Post.objects.get(pk=post_id)

        if is_user_post_shared(user, post) == False:
            post.shares.add(user)
            post.save()

        else:
            post.shares.remove(user)
            post.save()

        if user in post.shares.all():
            share_button_text = "UnShare"
        else:
            share_button_text = "Share"
        response = JsonResponse({'share_button_text': share_button_text})
        return response