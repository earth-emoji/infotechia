from django.urls import include, path

from . import views

urlpatterns = [
    path('tutorials/', include(([
        path('', views.tuts_list, name='list')
        # path('<slug:slug>/', views.profile_home, name='home'),
    ], 'tutorials'))),
]