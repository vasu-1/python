from django.shortcuts import render
from django.http.response import HttpResponse
from django.http import HttpResponse
# Create your views here.
from django import *

def home(request):
	# return HttpResponse("<h1>Hello World</h1>");
	return render(requst,'calc.html')

def add(request):
	val1 = request.POST['num1']
	val2 = request.POST['num2']
	res = int(val1) + int(val2)
	return render(request,'result.html',{'result':res})
	