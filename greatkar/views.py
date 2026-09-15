from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def login(request):
  if request.method == "POST":
    username = request.POST['username']
    password = request.POST['password']
    
    user = authenticate(
      request,
      username = username,
      password = password,
    )
    if user is not None:
      login(request,user)
      return redirect("index")
    else:
      return render(request,
                    'login.html',
                    {'error':"Invalid username and password"})
    
  return render(request,'login.html')
    
def index(request):
  return render(request,'index.html')   
    
    