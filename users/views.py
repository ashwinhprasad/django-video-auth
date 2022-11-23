from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout, authenticate, login


# Create your views here.
def LoginView(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('home')
	return render(request,'login.html',{})

def RegisterView(request):
	form = UserCreationForm()
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse("Account Created Successfully")
	return render(request,'register.html',{'form':form})


def LogoutView(request):
	logout(request)
	return redirect('home')