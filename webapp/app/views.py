from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.contrib.auth import authenticate, login as auth_login
from .models import *
# Create your views here.

def home(req):
    return render(req,'app/home.html')

def register(req):
    if req.method == "POST":
        username = req.POST['username']
        fname = req.POST['fname']
        lname = req.POST['lname']
        email = req.POST['email']
        pass1 = req.POST['pass1']
        
        myuser = User.objects.create_user(username,email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(req, "สร้างบัญชีเรียบร้อย ")    
        return redirect('registerXlogin')
    
    return render(req, "app/register.html")

def login(req):
    if req.method == 'POST':
        username = req.POST['username']
        pass1 = req.POST['pass1']
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            auth_login(req, user)
            fname = user.first_name
            return render(req, "app/home.html", {"fname": fname})
        else:
            messages.error(req, "ลองใหม่อีกครั้ง")
            return redirect('home')
    return render(req, 'app/login.html')

def registerXlogin(req):
    return render(req,'app/registerXlogin.html')


def signout(request):
    logout(request)
    return redirect('home')
