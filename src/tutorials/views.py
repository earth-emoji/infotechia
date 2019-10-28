from django.shortcuts import render, redirect

from .forms import TutorialForm
from .models import Tutorial

# Create your views here.
def tuts_list(request):
    template_name = 'tutorials/list.html'
    tuts = Tutorial.objects.all()
    search_term = ''
    if 'q' in request.GET:
        search_term = request.GET['q']
        tuts = tuts.filter(content__icontains=search_term)
    context = {
        'tuts': tuts,
        'search_term': search_term,
    }
    return render(request, template_name, context)

def tut_create(request):
    template_name = 'tutorials/tut_form.html'
    form = TutorialForm(request.POST or None)
    if form.is_valid():
        c = form.save(commit=False)
        c.author = request.user
        c.save()
        return redirect('tutorials:list')
    else:
        form = TutorialForm()
    return render(request, template_name, {'form': form})
