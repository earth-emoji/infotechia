from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework import status

from accounts.models import Professional
from jobs.forms import WorkHistoryForm
from jobs.models import WorkHistory
from jobs.serializers import WorkHistorySerializer
from users.decorators import professional_required

@login_required
@professional_required
def work_histories(request):
    template_name = 'work_history/list.html'
    context = {}
    work_history = WorkHistory.objects.filter(professional=request.user.professional)
    context["work_history"] = work_history
    return render(request, template_name, context)

@login_required
@professional_required
def work_create(request):
    template_name = 'work_history/form.html'
    context = {}
    if request.method == 'POST':
        form = WorkHistoryForm(request.POST or None)
        if form.is_valid():
            c = form.save(commit=False)
            c.professional = request.user.professional
            c.save()
            return redirect('work-history:list')
    else:
        form = WorkHistoryForm()
    context['form'] = form
    return render(request, template_name, context)

@login_required
@professional_required
@api_view(['GET', 'POST'])
def work_collection(request):

    if request.method == 'GET':
        work_history = WorkHistory.objects.filter(professional=request.user.professional)
        serializer = WorkHistorySerializer(work_history, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = {
            'employer_name': request.data.get('employer_name'),
            'start_date': request.data.get('start_date'),
            'end_date': request.data.get('end_date'),
            'job_title': request.data.get('job_title'),
            'duties': request.data.get('duties'),
            'professional': request.user.professional.pk
        }
        serializer = WorkHistorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
