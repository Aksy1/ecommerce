
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

def home(request):
    return render(request, 'category.html')
def user_login(request):
    if(request.method=="POST"):
        username=request.POST['u']
        password=request.POST['p']
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return home(request)
        else:
            messages.error(request,"Invalid user credentials")
    return render(request, 'login.html')
def register(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p = request.POST['p']
        cp = request.POST['cp']
        e = request.POST['e']
        f = request.POST['f']
        l = request.POST['l']
        if(p==cp):
            u=User.objects.create_user(username=u,password=p,email=e,first_name=f,last_name=l)
            u.save()
            return redirect('shop:home')
        else:
            messages.error(request,"Passwords not same")
    return render(request, 'register.html')

def user_logout(request):
    logout(request)
    return home(request)
