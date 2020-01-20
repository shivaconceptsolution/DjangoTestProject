from django.shortcuts import render
from django.http import HttpResponse
def index(request):
	return render(request,"patternapp/index.html")
def addition(request):
	return render(request,"patternapp/addition.html")
def addlogic(request):
	a=request.GET["txtnum1"]
	b=request.GET["txtnum2"]
	c=int(a)+int(b)
	return render(request,"patternapp/addition.html",{'res':c})
def fact(request):
	return render(request,"patternapp/fact.html")
def factlogic(request):
	a=request.GET["txtnum1"]
	f=1
	for i in range(1,int(a)+1):
		f=f*i
	return render(request,"patternapp/fact.html",{'res1':a,'res':f})


