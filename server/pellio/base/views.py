from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View



def index(request):
    return render(request, 'base/index.html')

def about(request):
    return render(request, 'base/about.html')

def registration(request):
    if request.method == "POST":
        pass #put the stuff here from the link Toshi gave. 
    return render(request, 'base/registration.html')

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

