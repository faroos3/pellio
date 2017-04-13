from django.contrib.auth.models import User
from django import forms

class UserRegistrationForm(forms.Form):
    FirstName = forms.CharField(
        required = False,
        label = 'First Name',
        max_length = 32,
    )
    LastName = forms.CharField(
        required = False,
        label = 'Last Name',
        max_length = 32, 
    )
    email = forms.CharField(
        required = True,
        label = 'Email',
        max_length = 32,
    )
    password = forms.CharField(
	required = True,
        label = 'Password',
        max_length = 32,
        widget = forms.PasswordInput()
    )
    rePassword = forms.CharField(
	required = True,
        label = 'Re-type Password',
        max_length = 32,
        widget = forms.PasswordInput()
    )

