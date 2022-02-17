from django.shortcuts import render
from travello.models import Destination
# Create your views here.

def index(request):
	# return render(request,'index.html')
	dest1 = Destination()
	dest1.name = "Nadiad"
	dest1.desc = "The lake of city"
	return render(request,'index.html',{'dest1':dest1})