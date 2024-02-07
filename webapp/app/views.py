import datetime
from django.shortcuts import render, redirect 
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,logout,login as auth_login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden , JsonResponse
from django.template import RequestContext
from django.db import IntegrityError
from .models import *
from .forms import *
from datetime import datetime


def home(req):
    return render(req,'app/home.html')


def registerXlogin(req):
    return render(req,'app/registerXlogin.html')


def signout(request):
    logout(request)
    return redirect('home')


def admin1(request):
    return render(request, 'admin/admin1.html', {'user': request.user})


def management(request):
    return render(request, 'admin/management.html', {'user': request.user})


def user_management_view(request):
    user_profiles = UserProfile.objects.all()
    return render(request, 'admin/management.html', {'user_profiles': user_profiles})


def register(req):
    if req.method == "POST":
        username = req.POST['username']
        fname = req.POST['fname']
        lname = req.POST['lname']
        email = req.POST['email']
        pass1 = req.POST['pass1']

        if User.objects.filter(username=username).exists():
            messages.error(req, "Username is already taken. Please choose a different username.")
            return render(req, "app/register.html")

        try:
            myuser = User.objects.create_user(username, email, pass1)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()

            UserProfile.objects.create(user=myuser, first_name=fname, last_name=lname, email=email, pass1=pass1)
            messages.success(req, "สร้างบัญชีเรียบร้อย ")
            return redirect('login')

        except IntegrityError:
            messages.error(req, "An error occurred while creating the user. Please try again.")
            return render(req, "app/register.html")

    return render(req, "app/register.html")


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass1')
        user = authenticate(username=username, password=password)

        if user is not None:
            auth_login(request, user)

            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': True, 'message': 'Login successful'})
            else:
                fname = user.first_name
                return render(request, "app/home.html", {"fname": fname})
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'message': 'Invalid credentials'})
            else:
                messages.error(request, "Invalid credentials")
                return redirect('home')

    return render(request, 'app/login.html')


@login_required
def edit_profile(request):
    user_profile = request.user.userprofile

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            day = request.POST.get('day')
            month = request.POST.get('month')
            year = request.POST.get('year')
            birth_date_str = f"{year}-{month}-{day}"
            birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d").date()
            user_profile.birth_date = birth_date
            user_profile.save()
            messages.success(request, 'บันทึกข้อมูลเรียบร้อยแล้ว')
            return redirect('profile')
        else:
            messages.error(request, 'กรุณากรอกข้อมูลที่ถูกต้อง')
    else:
        form = UserProfileForm(instance=user_profile)
    return render(request, 'app/edit_profile.html', {'form': form})


@login_required
def upload_profile_image(request):
    if request.method == 'POST':
        profile_image = request.FILES.get('profile_image')
        if profile_image:
            request.user.userprofile.profile_image = profile_image
            request.user.userprofile.save()
            messages.success(request, 'อัพโหลดโปรไฟล์เรียบร้อยแล้ว')
        else:
            messages.error(request, 'กรุณาเลือกรูปภาพ')
    return redirect('profile')


@login_required
def profile(request):
    return render(request, 'app/profile.html', {'user': request.user})


