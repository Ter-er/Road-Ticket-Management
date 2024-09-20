from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('motorist_signup/', views.motorist_signup, name='motorist_signup'),
    path('motorist_login/', views.motorist_login, name='motorist_login'),
    path('official_signup/', views.official_signup, name='official_signup'),
    path('official_login/', views.official_login, name='official_login'),
    path('admin_login/', views.admin_login_redirect, name='admin_login_redirect'),
    # Add other URL patterns here
]
