import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from datetime import datetime
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
        
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()

        UserProfile.objects.create(user=myuser, first_name=fname, last_name=lname, email=email)

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

def profile(request):
    return render(request, 'app/profile.html', {'user': request.user})

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
def edit_profile(request):
    user_profile = request.user.userprofile

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            # ดึงข้อมูลวันที่, เดือน, และปีจาก form
            day = request.POST.get('day')
            month = request.POST.get('month')
            year = request.POST.get('year')

            # นำวันที่, เดือน, และปีมารวมกันเพื่อสร้างวันที่แบบ Python
            birth_date_str = f"{year}-{month}-{day}"
            birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d").date()

            # กำหนดค่าวันเกิดใน UserProfile และบันทึก
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
