from django.urls import include, path

from . import views

urlpatterns = [
    path('projects/', include(([
        path('create/', views.create_problem, name='create'),
        path('<slug:slug>/', views.problem_details, name='details'),
    ], 'projects'))),
]