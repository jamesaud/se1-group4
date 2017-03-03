from django.http import HttpResponse
from django.shortcuts import render
from allauth.account.forms import SignupForm
from allauth.account.views import SignupView
from .models import Employer
from .forms import EmployerForm
from django.shortcuts import redirect

def index(request):
    return HttpResponse("MADE IT!")


def account_signup(request):
    context = {'form': SignupForm()}
    return render(request, 'account/signup_company.html', context=context)


class SignUp(SignupView):

    def form_valid(self, form):
        response = super().form_valid(form)
        employer = Employer(user=self.user)
        employer.save()
        return response


def home(request, username):
    return render(request, 'employers/home.html')


def update(request):
    form = EmployerForm(request.POST or None, instance = request.user.employer)
    if (request.method == 'POST') and form.is_valid():
        for key, value in form.cleaned_data.items():
            setattr(request.user.employer, key, value)
        request.user.employer.save()
        return redirect('employers:home', username=request.user.username)

    return render(request, 'employers/employer_form.html', context={'form': form})

