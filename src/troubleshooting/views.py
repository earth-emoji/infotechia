from django.shortcuts import render, redirect

from .forms import ProblemForm
from .models import Problem, Cause, Question, Solution

# Create your views here.
def create_problem(request):
    template_name = 'troubleshooting/problem_form.html'
    if request.method == 'POST':
        form = ProblemForm(request.POST or None)
        if form.is_valid():
            c = form.save(commit=False)
            c.problem_solver = request.user.profile
            c.save()
            return redirect("projects:details", c.slug)
    else:
        form = ProblemForm()
    return render(request, template_name, {'form': form})

def problem_details(request, slug):
    template_name = 'troubleshooting/problem_details.html'
    problem = Problem.objects.get(slug=slug)
    context = {
        'problem': problem
    }
    return render(request, template_name, context)
