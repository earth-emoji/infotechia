from django.contrib.auth import logout, login
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.edit import CreateView

from troubleshooting.models import Problem

from accounts.forms import UserSignUpForm
from accounts.models import UserProfile
from users.models import User


class UserSignUpView(CreateView):
    model = User
    form_class = UserSignUpForm
    template_name = 'registration/signup_form.html'

    # def get_context_data(self, **kwargs):
    #     kwargs['user_type'] = 'User'
    #     return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('workspace:home', self.request.user.profile.slug)


def logout_view(request):
    logout(request)
    return redirect('home')


def workspace_home(request, slug):
    template_name = 'workspace/home.html'
    profile = UserProfile.objects.get(slug=slug)
    problems = Problem.objects.filter(problem_solver=profile)
    context = {
        'profile': profile,
        'problems': problems,
    }
    return render(request, template_name, context)
