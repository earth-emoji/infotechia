from django.shortcuts import render, redirect

from .forms import ThreadForm
from .models import Topic, Thread

# Create your views here.
def topic_list(request):
    template_name = "topics/list.html"
    topics = Topic.objects.all()
    search_term = ''
    if 'q' in request.GET:
        search_term = request.GET['q']
        topics = topics.filter(name__icontains=search_term)
    context = {
        'topics': topics,
        'search_term': search_term,
    }
    return render(request, template_name, context)

def thread_list(request, slug):
    topic = Topic.objects.get(slug=slug)
    template_name = "threads/list.html"
    threads = Thread.objects.filter(topic=topic)
    search_term = ''
    if 'q' in request.GET:
        search_term = request.GET['q']
        threads = threads.filter(body__icontains=search_term)
    context = {
        'topic': topic,
        'threads': threads,
        'search_term': search_term,
    }
    return render(request, template_name, context)

def thread_create(request, slug):
    template_name = 'threads/thread_form.html'
    topic = Topic.objects.get(slug=slug)
    if request.method == 'POST':
        form = ThreadForm(request.POST or None)
        if form.is_valid():
            c = form.save(commit=False)
            c.topic = topic
            c.creator = request.user
            c.save()
            return redirect("topics:threads", topic.slug)
    else:
        form = ThreadForm()
    return render(request, template_name, {'form': form})