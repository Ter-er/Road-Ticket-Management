from django.urls import path
from .views import SignUpView, LoginView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('dashboard/motorist/', motorist_dashboard_view, name='motorist_dashboard'),
    path('dashboard/admin/', admin_dashboard_view, name='admin_dashboard'),
    path('dashboard/official/', official_dashboard_view, name='official_dashboard'),
]