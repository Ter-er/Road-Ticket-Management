# User/urls.py
from django.urls import path
from .views import sign_up, login, motorist_dashboard_view

urlpatterns = [
    path('signup/', sign_up, name='signup'),
    path('login/', login, name='login'),
    path('dashboard/motorist/', motorist_dashboard_view, name='motorist_dashboard'),
]
