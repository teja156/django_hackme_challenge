from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm

#Create your views here.

def register(request):

	if (not(request.user.is_authenticated)):
		form = UserCreationForm
		return render(request,'register/register.html')
	else:
		return redirect('dashboard')

def process_registration(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if(form.is_valid()):
			uname = form.cleaned_data['username']
			passwd = form.cleaned_data['password1']
			user = User.objects.create_user(username=uname, password= passwd)


			return HttpResponse("<h1>Registered Succesfully!.<a href='/login'>Login here</a></h1>")

		else:
			return render(request,'register/register.html',context={'err_msg':'Failed to register. Either the username already exists or you are not following the rules for registration fields.'})

	else:
		return HttpResponse("<h1>Only Post method allowed!</h1>")






