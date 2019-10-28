from django.urls import include, path

from . import views

urlpatterns = [
    path('topics/', include(([
        path('', views.topic_list, name='list'),
        path('<slug:slug>/discussions/', views.thread_list, name='threads'),
        # path('<slug:slug>/', views.profile_home, name='home'),
    ], 'topics'))),
    path('<slug:slug>/discussions/', include(([
        path('create/', views.thread_create, name='create'),
    ], 'threads'))),
]