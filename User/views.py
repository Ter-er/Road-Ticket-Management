# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.views import View
from .forms import MotoristSignUpForm, AdminOfficialSignUpForm, MotoristLoginForm, AdminOfficialLoginForm
from django.contrib.auth.models import Group

# Motorist/Admin/Official Sign Up
def sign_up(request):
    if request.method == 'POST':
        if 'license_no' in request.POST:  # Motorist
            form = MotoristSignUpForm(request.POST)
        else:  # Admin/Official
            form = AdminOfficialSignUpForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            if 'license_no' in request.POST:
                user.set_password(form.cleaned_data['license_no'])  # Motorist password is license_no
                motorist_group = Group.objects.get(name='Motorist')  # Assuming group for Motorists
                motorist_group.user_set.add(user)
            else:
                user.set_password(form.cleaned_data['password'])  # Admin/Official use password
                # Admin/Official group assignment can go here

            user.save()
            auth_login(request, user)
            return redirect('dashboard')
    else:
        if 'license_no' in request.GET:  # Motorist
            form = MotoristSignUpForm()
        else:  # Admin/Official
            form = AdminOfficialSignUpForm()

    return render(request, 'signup.html', {'form': form})

# Motorist/Admin/Official Login
def login(request):
    if request.method == 'POST':
        if 'license_no' in request.POST:  # Motorist
            form = MotoristLoginForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data['email']
                license_no = form.cleaned_data['license_no']
                user = authenticate(request, email=email, password=license_no)  # Authenticate Motorist by license_no
        else:  # Admin/Official
            form = AdminOfficialLoginForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                user = authenticate(request, email=email, password=password)  # Authenticate Admin/Official by password

        if user is not None:
            auth_login(request, user)
            return redirect('dashboard')  # Redirect to respective dashboard
    else:
        if 'license_no' in request.GET:  # Motorist
            form = MotoristLoginForm()
        else:  # Admin/Official
            form = AdminOfficialLoginForm()

    return render(request, 'login.html', {'form': form})

# Placeholder for motorist dashboard view
def motorist_dashboard_view(request):
    return render(request, 'dashboard_motorist.html')
