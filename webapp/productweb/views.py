from django.shortcuts import get_object_or_404, render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import authenticate, login as auth_login
from app.models import *
from .models import *

# Create your views here.


def products(request):
    all_products = item.objects.all()
    context = {'products': all_products}
    return render(request, 'productweb/product.html', context)


def product(request, item_id):
    item_instance = get_object_or_404(item, id=item_id)
    return render(request, 'productweb/product_detail.html', {'item': item_instance})

def contag(req):
    return render(req,'productweb/contag.html')