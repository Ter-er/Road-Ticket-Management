from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from .forms import MotoristSignUpForm, AdminOfficialSignUpForm, MotoristLoginForm, AdminOfficialLoginForm

def sign_up(request):
    if request.method == 'POST':
        if 'license_no' in request.POST:  # Motorist
            form = MotoristSignUpForm(request.POST)
        else:  # Admin/Official
            form = AdminOfficialSignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        if 'license_no' in request.GET:  # Motorist
            form = MotoristSignUpForm()
        else:  # Admin/Official
            form = AdminOfficialSignUpForm()

    return render(request, 'User/sign_up.html', {'form': form})

def login(request):
    if request.method == 'POST':
        if 'license_no' in request.POST:  # Motorist
            form = MotoristLoginForm(request.POST)
        else:  # Admin/Official
            form = AdminOfficialLoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)

            if user is not None:
                auth_login(request, user)
                return redirect('dashboard')  # Redirect to dashboard or home page
    else:
        if 'license_no' in request.GET:  # Motorist
            form = MotoristLoginForm()
        else:  # Admin/Official
            form = AdminOfficialLoginForm()

    return render(request, 'User/login.html', {'form': form})