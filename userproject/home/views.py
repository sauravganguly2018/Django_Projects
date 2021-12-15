from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'index.html')

def loginUser(request):
    if request.method=="POST":
        Username=request.POST.get('username')
        Password=request.POST.get('password')

        user = authenticate(username=Username, password=Password)
        if user is not None:
            # A backend authenticated the credentials
            login(request,user)
            return redirect("/")
        else:
            # No backend authenticated the credentials
            return redirect("/login")
    
    if request.user.is_anonymous:
        return render(request,'login.html')
    return redirect("/")

def logoutUser(request):
    logout(request)
    return redirect("/login")
