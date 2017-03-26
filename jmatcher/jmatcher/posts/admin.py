from django.contrib.admin import AdminSite
from django.contrib import admin

from .forms import PostForm
from .models import Post
from .models import PostComments
from .models import PostShares
from .models import PostLikes

admin.site.register(Post)
admin.site.register(PostComments)
admin.site.register(PostShares)
admin.site.register(PostLikes)