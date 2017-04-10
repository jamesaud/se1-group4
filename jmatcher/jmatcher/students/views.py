from django.http import HttpResponse
from django.shortcuts import render
from allauth.account.views import SignupView, SignupForm
from .models import Student
from .forms import StudentForm
from django.shortcuts import redirect
from jmatcher.users.forms import UserForm
from jmatcher.users.models import Skill, User

def index(request):
    return HttpResponse("MADE IT!")



def account_signup(request):
    context = {'form': SignupForm()}
    return render(request, 'account/signup_student.html', context=context)



class SignUp(SignupView):

    def form_valid(self, form):
        response = super(SignUp, self).form_valid(form)
        student = Student(user=self.user)
        student.save()
        return response


def home(request, username):
    student = User.objects.get(username=username).student
    return render(request, 'students/home.html', context={'object': student})


def update(request):
    form = StudentForm(request.POST or None, instance = request.user.student)

    user_form = UserForm(request.POST or None, instance=request.user)
    if (request.method == 'POST') and form.is_valid() and user_form.is_valid():
        skills = form.cleaned_data['skill']

        for key, value in form.cleaned_data.items():
            setattr(request.user.student, key, value)

        for key, value in user_form.cleaned_data.items():
            setattr(request.user, key, value)

        request.user.image = user_form.cleaned_data['image']

        for skill in form.cleaned_data['skill'].split(","):
            skill = skill.strip().lower()
            try:
                skill_object = Skill.objects.get(skill=skill)
            except Skill.DoesNotExist as e:
                skill_object = Skill(skill=skill)
                skill_object.save()
            else:
                request.user.student.skills.add(skill_object)

        request.user.student.save()
        request.user.save()

        return redirect('students:home', username=request.user.username)

    return render(request, 'students/student_form.html', context={'form': form,
                                                                  'user_form':user_form})

