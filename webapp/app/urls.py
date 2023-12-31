"""
URL configuration for webapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
from .views import *
from django.urls import path


urlpatterns = [
    path('' , views.home, name='home'),
    path('signout', views.signout, name='signout'),
    path('registerXlogin', views.registerXlogin, name='registerXlogin'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('upload_profile_image/', upload_profile_image, name='upload_profile_image'),
    path('profile/', profile, name='profile'),
    path('profile/edit/', edit_profile, name='edit_profile'),
    path('admin1/', admin1, name='admin1'),
    path('management/', views.management, name='management'),
    path('user_management/', user_management_view, name='user_management'),

]
