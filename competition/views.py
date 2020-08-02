from django.shortcuts import render,redirect,reverse
from .models import team
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.views import View
from django.contrib.auth.decorators import login_required
from .forms import TeamForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def register(request):
	if request.method == "POST":
		form = TeamForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("registered")
		else:
			print(form.errors)
			return redirect("register")
	else:		
		return render(request,"registration_form.html", {"forms": TeamForm()})

def registered(request):
	return render(request, 'registered.html')

def universities(request):
    teams = team.objects.all()
    return render(request, "university list.html", {'teams': teams})

def teamDetails(request, name):
    teams = team.objects.get(name=name)
    return render(request, 'teamDetails.html', {'team': teams})