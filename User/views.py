from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse
from .forms import MotoristSignUpForm, MotoristLoginForm, OfficialSignUpForm, OfficialLoginForm
from .models import User

def home(request):
    return render(request, 'home.html')

# Motorist views
def motorist_signup(request):
    if request.method == 'POST':
        form = MotoristSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('motorist_login')
    else:
        form = MotoristSignUpForm()
    return render(request, 'motorist_signup.html', {'form': form})

def motorist_login(request):
    if request.method == 'POST':
        form = MotoristLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            license_no = form.cleaned_data['license_no']
            try:
                user = User.objects.get(email=email, license_no=license_no, role='motorist')
                login(request, user)  # Use Django's login method
                return redirect('dashboard_motorist')  # Redirect to the motorist dashboard
            except User.DoesNotExist:
                form.add_error(None, 'Invalid email or license number')
    else:
        form = MotoristLoginForm()
    return render(request, 'motorist_login.html', {'form': form})

# Official views
def official_signup(request):
    if request.method == 'POST':
        form = OfficialSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('official_login')
    else:
        form = OfficialSignUpForm()
    return render(request, 'official_signup.html', {'form': form})

def official_login(request):
    if request.method == 'POST':
        form = OfficialLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user and user.role == 'official':
                login(request, user)
                return redirect('dashboard_official')  # Redirect to the official dashboard
            else:
                form.add_error(None, 'Invalid email or password')
    else:
        form = OfficialLoginForm()
    return render(request, 'official_login.html', {'form': form})

# Admin views
def admin_login_redirect(request):
    return redirect(reverse('admin:login'))
