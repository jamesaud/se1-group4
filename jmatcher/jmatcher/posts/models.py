from django.db import models
from jmatcher.users.models import User

#Create your models here

class Post(models.Model):

    user = models.ForeignKey(User)
    description = models.CharField(max_length=1000)
    image = models.ImageField(null=True)  # Need to limit file size


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def get_comment_count(self):
        return len(self.postcomments_set)

    def get_share_count(self):
        return len(self.postshares_set)

    def __str__(self):
        return self.description


class PostComments(models.Model):

    commenting_user = models.ForeignKey(User)  # The commenting user
    post = models.ForeignKey(Post)
    comment = models.CharField(max_length=250)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class PostShares(models.Model):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    sharing_user = models.ForeignKey(User)  # The sharing user
    post = models.ForeignKey(Post)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class PostLikes(models.Model):

    sharing_user = models.ForeignKey(User)  # The sharing user
    post = models.ForeignKey(Post)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)