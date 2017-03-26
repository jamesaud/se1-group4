from django.db import models
from jmatcher.users.models import User

#Create your models here

class Post(models.Model):

    user = models.ForeignKey(User)
    description = models.CharField(max_length=1000)
    image = models.ImageField(null=True)  # Need to limit file size
    '''
    https://docs.djangoproject.com/en/1.10/topics/db/examples/many_to_many/
    https://docs.djangoproject.com/en/dev/topics/db/queries/#backwards-related-objects
    http://stackoverflow.com/questions/2642613/what-is-related-name-used-for-in-django
    '''

    likes = models.ManyToManyField(User, related_name="likes")
    shares = models.ManyToManyField(User, related_name="shares")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def get_comment_count(self):
        return self.postcomments_set.count()

    def total_likes(self):
        return self.likes.count()

    def total_shares(self):
        return self.shares.count()

    def __str__(self):
        return self.description


class PostComments(models.Model):

    commenting_user = models.ForeignKey(User)  # The commenting user
    post = models.ForeignKey(Post)
    comment = models.CharField(max_length=250)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)