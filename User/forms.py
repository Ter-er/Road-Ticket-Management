from django import forms
from .models import User

class MotoristSignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'license_no', 'first_name', 'last_name']  # Exclude password

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'motorist'  # Set role to motorist
        if commit:
            user.save()
        return user

class MotoristLoginForm(forms.Form):
    email = forms.EmailField()
    license_no = forms.CharField(max_length=20)

class AdminOfficialSignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name']  # Exclude license_no

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