
from django import forms
from django.contrib.auth import views as auth_views
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View

from .forms import UserRegistrationForm


def index(request):

    return render(request, 'base/index.html', { 'page':"Pellio"})

def home(request):

    return render(request, 'base/home.html' , { 'page':"Home" })

def about(request):

    return render(request, 'base/about.html')

def experiments(request):
    return render( request, 'base/experiments.html')

def registration(request):

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            email =  userObj['email']
            password =  userObj['password']
            if not (User.objects.filter(email=email).exists() ):
                User.objects.create_user( email, password)
                user = authenticate(email = email, password = password)
                login(request, user)
                return HttpResponseRedirect('/Home')
            else:
                raise forms.ValidationError('Looks like a username with that email or password already exists')

    else:
        form = UserRegistrationForm()

	return render(request, 'base/registration.html', {'form' : form, "page":"Registration"})
