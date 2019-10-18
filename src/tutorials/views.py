from django.shortcuts import render

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