from django.shortcuts import render, redirect

# Create your views here.
def home(request, template_name='pages/home.html'):
    if request.user.is_authenticated:
        return redirect('workspace:home', request.user.profile.slug)
    return render(request, template_name)
