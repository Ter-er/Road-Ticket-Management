from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class MotoristSignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'license_no', 'first_name', 'last_name']  # Include email and license_no

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'motorist'  # Set role to motorist
        if commit:
            user.save()
        return user

class MotoristLoginForm(forms.Form):
    email = forms.EmailField()
    license_no = forms.CharField(max_length=20)

class OfficialSignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name']  # Include email and password

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'official'  # Set role to official
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class OfficialLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

class AdminOfficialSignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name']  # Include email and password

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'admin'  # Default role for example
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class AdminOfficialLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
