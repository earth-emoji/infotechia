from django.urls import include, path

from . import views

urlpatterns = [
    path('logout/', views.logout_view, name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.UserSignUpView.as_view(), name='user_signup'),
    path('workspace/', include(([
        path('<uuid:slug>/', views.workspace_home, name='home'),
    ], 'workspace'))),
]