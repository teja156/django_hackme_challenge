from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import pickle
import base64
from django.contrib.auth import logout

# Create your views here.

def login_screen(request):
	if request.user.is_authenticated:
		return redirect("dashboard")
	else:	
		return render(request,'login/login.html')


def authenticate_user(request):
	if request.method=="POST":
		uname = request.POST['uname']
		passwd = request.POST['passwd']
		print(uname)

		user = authenticate(username=uname, password=passwd)
		

		pickled_cookie = base64.urlsafe_b64encode(pickle.dumps(uname))

		if user is not None:
			#assign some sessions
			login(request,user)
			
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
