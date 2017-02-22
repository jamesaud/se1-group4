from django.http import HttpResponse
from django.shortcuts import render
from allauth.account.forms import SignupForm

def index(request):
    return render(request, 'employers/home.html', context={})


def account_signup(request):
    if request.user.is_authenticated:
        return HttpResponse("HELLO")
    context = {'form': SignupForm()}
    context['redirect_field_name'] = 'employers/account_signup'
    context['redirect_field_value'] = 'employers/account_signup'
    return render(request, 'account/signup.html', context=context)
