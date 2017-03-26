from django.contrib.admin import AdminSite
from django.contrib import admin

from .forms import PostForm
from .models import Post
from .models import PostComments

admin.site.register(Post)
admin.site.register(PostComments)
