from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

#Create your views here.

def register(request):
	return render(request,'register/register.html')

def process_registration(request):
	if request.method == "POST":
		uname = request.POST['uname']
		passwd = request.POST['passwd']
		email = request.POST['email']

		user = User.objects.create_user(uname, email, passwd)


		if user is not None:
		    # A backend authenticated the credentials
		    return HttpResponse("<h1>Registered Succesfully!.<a href='/'>Login here</a></h1>")
		else:
		    # No backend authenticated the credentials
		    return HttpResponse("Couldn't register!")

	else:
		return HttpResponse("<h1>Only Post method allowed!</h1>")



