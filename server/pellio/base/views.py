from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

#def index(request):
    #return HttpResponse("<h2>Hello, world. You're at the homepage? index.</h2>")

def index(request):
    return render(request, 'base/index.html')

def about(request):
    return render(request, 'base/about.html')

def registration(request):
    if request.method == "POST":
        pass #put the stuff here from the link Toshi gave. 
    return render(request, 'base/registration.html')
