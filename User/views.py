from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import MotoristSignUpForm, MotoristLoginForm, OfficialSignUpForm, OfficialLoginForm
from .models import User
from Ticket.models import Ticket


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

            # Use the custom backend to authenticate the user
            user = authenticate(request, email=email, license_no=license_no)

            if user is not None:
                login(request, user)  # Log the user in
                return redirect('dashboard_motorist')  # Redirect to the motorist dashboard
            else:
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

@login_required
def dashboard_motorist(request):
    user = request.user
    if user.role != 'motorist':  # Ensure only motorists can access this page
        return redirect('motorist_login')
    
    tickets = Ticket.objects.filter(motorist=user)  # Assuming you have a Ticket model
    total_points = tickets.aggregate(Sum('points'))['points__sum'] or 0  # Sum of offense points

    context = {
        'first_name': user.first_name,
        'last_name': user.last_name,
        'license_no': user.license_no,
        'points': total_points,
        'tickets': tickets
    }
    return render(request, 'dashboard_motorist.html', context)