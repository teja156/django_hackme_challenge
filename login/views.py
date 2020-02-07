from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import pickle
import base64
from django.contrib.auth import logout
from . import get_ip
from ipware import get_client_ip
from . models import CrackedUsers

# Create your views here.

def login_screen(request):
	if request.user.is_authenticated:
		return redirect("dashboard")
	else:	
		return render(request,'login/login.html')


def authenticate_user(request):

	ip, is_routable = get_client_ip(request)
	if ip is not None:
		print("IP address = ",ip)
		print("Routable : ",is_routable)
	if request.method=="POST":
		uname = request.POST['uname']
		passwd = request.POST['passwd']
		print(uname)

		user = authenticate(username=uname, password=passwd)
		

		pickled_cookie = base64.urlsafe_b64encode(pickle.dumps(uname))

		if user is not None:
			#assign some sessions
			login(request,user)
			request.session['cracked'] = '0'
			
			response = redirect('dashboard')
			response.set_cookie('unamepickled',pickled_cookie.decode())

			return response
		else:

			return render(request,'login/login.html',context={'err_msg':'Invalid Username/Password.'})
	else:
		return HttpResponse("Only POST method allowed.")


@login_required
def dashboard(request):
	uname_pickled = request.COOKIES.get('unamepickled').encode() #convert to bytes
	print(uname_pickled)

	#decode data
	dec_data = base64.urlsafe_b64decode(uname_pickled)

	uname = pickle.loads(dec_data)


	return render(request,'login/dashboard.html',context={'uname':uname})


def logout_view(request):
	logout(request)

	return redirect('/login')

def show_home(request):
	return render(request,'app/index_hackme.html')

def show_app_screen(request):
	return render(request,'app/app.html')

def submit_key_screen(request):
	return render(request,'app/submitkey.html')

@login_required
def submit_key(request):
	if request.method=="POST":
		f = open('login/secret_key.txt','r')
		key = f.read()
		f.close()
		submitted_key = request.POST['secret_key']

		print("submitted : ",submitted_key)
		print("real " ,key)
		if(submitted_key.strip()==key.strip()):
			print("matched")
			request.session['cracked'] = '1'
			return redirect(get_featured)
		else:
			return render(request,'app/submitkey.html',context={'err_msg' : 'Wrong key'})

	else:
		return HttpResponse("Only POST requests allowed on this page.")


@login_required
def feature_user(request):
	if(request.session['cracked']=='1'):
		name = request.POST['name']
		profile = request.POST['profile']

		cu = CrackedUsers(name=name,profile_link=profile)
		cu.save()

		return redirect(solved_by)

	else:
		return HttpResponse("You did not solve the challenge. <a href='/'>go home</a>")

@login_required
def get_featured(request):
	return render(request,'app/submitcrackeduserdetails.html')

def solved_by(request):
	return render(request,'app/solvedby.html',context={'users' : CrackedUsers.objects.all()})

