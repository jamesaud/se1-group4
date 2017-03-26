from django.db import models


from django.contrib.auth.models import AbstractUser

"""
Everything Below goes in the Users App
"""
class User(AbstractUser):
    """
    AbstractUser comes built-in with first_name, last_name, email, password, and many other fields at:
    https://docs.djangoproject.com/en/1.10/ref/contrib/auth/
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




class Student(User):

    location = models.OneToOneField(Location)
    connections = models.ManyToManyField("self")
    skills = models.ManyToManyField(Skill)


SIZE_CHOICES = (
    ('0', '1-50'),
    ('1', '51-100'),
    ('2', '101-1000'),
)

class Company(User):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    company_name = models.CharField()
    location = models.OneToOneField(Location)
    website = models.URLField()
    size = models.CharField(choices=SIZE_CHOICES)
    description = models.CharField()


class Location(models.Models):
    city = models.CharField()
    state = models.CharField()


class Skill(models.Model):
    skill = models.CharField()


class Education(models.Model):

    user = models.ForeignKey(Student)
    level = models.CharField() # Choices
    institution_name = models.CharField()
    start_year = models.IntegerField()
    end_year = models.IntegerField()   # Enforce that end_year comes after start_year.


class WorkExperience(models.Model):

    user = models.ForeignKey(Student)
    title = models.CharField()
    status = models.CharField() # Choise of 'intern' or 'full time'
    start_date = models.DateField()
    end_date = models.DateField()   # Enforce that end_date comes after start_date.
    description = models.CharField()


"""
Job goes in the Job App
"""
class Job(models.Model):
    company = models.ForeignKey(Company)
    description = models.CharField()
    experience_preferred = models.CharField()
    experience_desired = models.CharField()
    required_work_experience = models.IntegerField(default=0)
    skills = models.ManyToManyField(Skill)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



"""
Post goes in the 'Feed App'
"""
class Post(models.Model):

    user = models.ForeignKey(User)
    description = models.CharField()
    image = models.ImageField()  # Need to limit file size


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def get_comment_count(self):
        return len(self.postcomments_set)

    def get_share_count(self):
        return len(self.postshares_set)


class PostComments(models.Model):

    commenting_user = models.ForeignKey(User)  # The commenting user
    post = models.ForeignKey(Post)
    comment = models.CharField()

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


"""
TODO:  Messages
Goes in the 'Messages App'
"""
