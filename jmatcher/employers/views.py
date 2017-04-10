from django.http import HttpResponse
from django.shortcuts import render
from allauth.account.forms import SignupForm
from allauth.account.views import SignupView
from .models import Employer
from jmatcher.users.models import User
from .forms import EmployerForm, EmployerUserForm
from django.shortcuts import redirect

def index(request):
    return HttpResponse("MADE IT!")


def account_signup(request):
    context = {'form': SignupForm()}
    return render(request, 'account/signup_company.html', context=context)


class SignUp(SignupView):

    def form_valid(self, form):
        response = super().form_valid(form)
        print("im emplyoer")
        employer = Employer(user=self.user)
        print("HE")
        employer.save()
        print("NOW ERE")
        print("I AM AN EMPLOYER")
        print(employer.__dict__)
        print(employer.user)
        return response


def home(request, username):
    object = User.objects.get(username=username).employer
    jobs = object.user.job_set.all()
    return render(request, 'employers/home.html', context={'object':object, 'jobs' : jobs})


def update(request):
    form = EmployerForm(request.POST or None, instance = request.user.employer)
    user_form = EmployerUserForm(request.POST or None, request.FILES or None, instance=request.user)
    if (request.method == 'POST') and form.is_valid() and user_form.is_valid():
        print(user_form.is_valid())

        for key, value in form.cleaned_data.items():
            setattr(request.user.employer, key, value)
        request.user.employer.save()

        for key, value in user_form.cleaned_data.items():
            setattr(request.user, key, value)
        if user_form.cleaned_data['image']:
            request.user.image = user_form.cleaned_data['image']
        request.user.save()

        return redirect('employers:home', username=request.user.username)

    return render(request, 'employers/employer_form.html', context={'form': form, 'user_form': user_form})



def list(request):
    return render(request, 'employers/employer_list.html',
           context={'employer_list': Employer.objects.exclude(company_name__isnull=True)})

