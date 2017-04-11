# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import HttpResponse, redirect
from django.contrib import messages

from .models import User
from jmatcher.students.models import Student


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = 'username'
    slug_url_kwarg = 'username'




class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        if self.request.user.is_employer():
            return reverse('employers:home',
                           kwargs={'username': self.request.user.username})
        elif self.request.user.is_student():
            return reverse('students:home',
                           kwargs={'username': self.request.user.username})

        else:
            student = Student(user=self.request.user)
            student.save()
            return reverse('students:home',
                           kwargs={'username': self.request.user.username})

class UserUpdateView(LoginRequiredMixin, UpdateView):

    fields = ['name', ]

    # we already imported User in the view code above, remember?
    model = User

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})

    def get_object(self):
        # Only get the User record for the user making the request
        return User.objects.get(username=self.request.user.username)


class UserListView(LoginRequiredMixin, ListView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = 'username'
    slug_url_kwarg = 'username'




def ajaxview(request):
    if request.method == 'POST':
        return HttpResponse(request.POST.items())


def follow(request, username):
    if request.method == 'GET':
        user = User.objects.get(username=username)
        request.user.connections.add(user)
        request.user.save()
        messages.success(request, 'Following ' + str(user))
        if request.GET.get('redirect_url'):
            return redirect(request.GET.get('redirect_url'))
        else:
            return redirect(user.get_absolute_url())

def unfollow(request, username):
    if request.method == 'GET':
        user = User.objects.get(username=username)
        request.user.connections.remove(user)
        request.user.save()
        messages.success(request, 'Unfollowed ' + str(user))
        if request.GET.get('redirect_url'):
            return redirect(request.GET.get('redirect_url'))
        else:
            return redirect(user.get_absolute_url())

