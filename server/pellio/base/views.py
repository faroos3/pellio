
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django import forms
from .forms import UserRegistrationForm


def index(request):
    if request.method == "POST":
        pass #put the stuff here from the link Toshi gave. 
    return render(request, 'base/index.html', { 'page':"Pellio"})

def about(request):
    return render(request, 'base/about.html')

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email =  userObj['email']
            password =  userObj['password']
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)
                user = authenticate(username = username, password = password)
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                raise forms.ValidationError('Looks like a username with that email or password already exists')

    else:
        form = UserRegistrationForm()

	return render(request, 'base/registration.html', {'form' : form, "page":"Registration"})

"""class UserFormView(View):
	form_class = UserForm
	template_name = 'register.html'

	#display blank form 
	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form})
	
	def post(self, request):
		form = self.form_class(request.POST)
		
		if form.is_valid():
			
			user = form.save(commit=False)
		
			# cleaned (normalized) data
			firstName = form.cleaned_data['firstName']
			lastName = form.cleaned_data['lastName']
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()

			#returns User objects if credentials are correct
			User = authenticate(firstName= firstName, password= password)
			
			if user is not None:
				
				if user.is_active:
				
					login(request, user)
					return redirect('base:index')
		return render(request, self.template_name, {'form': form}
"""			

