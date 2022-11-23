from django.shortcuts import render
from .models import videosModel
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/users/signin/')
def HomeView(request):
	return render(request,'index.html',{'videos':videosModel.objects.all()})