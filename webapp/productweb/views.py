from django.shortcuts import get_object_or_404, render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,logout,login as auth_login
from django.contrib.auth.decorators import login_required
from app.models import *
from .forms import *
from .models import *
from django.http import JsonResponse
from django.urls import reverse
from django.http import HttpResponseRedirect


def products(request):
    all_products = Item.objects.all()
    context = {'products': all_products}
    return render(request, 'productweb/product.html', context)


def product(request, item_id):
    item_instance = get_object_or_404(Item, id=item_id)
    return render(request, 'productweb/product_detail.html', {'item': item_instance})

def add_product(request):
    if request.method == 'POST':
        item_form = ItemForm(request.POST)
        image_form = ItemImageForm(request.POST, request.FILES)

        if item_form.is_valid() and image_form.is_valid():
            item = item_form.save()
            image = image_form.save(commit=False)
            image.item = item
            image.save()

            return redirect('products') 
    else:
        item_form = ItemForm()
        image_form = ItemImageForm()

    return render(request, 'productweb/add_product.html', {'item_form': item_form, 'image_form': image_form})

def delete_product(request, product_id):
    product = get_object_or_404(Item, id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('products') 

    return render(request, 'productweb/delete_product.html', {'product': product})
@login_required
def cart(req):
    try:
        # ค้นหา UserProfile สำหรับผู้ใช้งานปัจจุบัน
        user_profile = UserProfile.objects.get(user=req.user)
        # ค้นหาหรือสร้างตะกร้าสำหรับ UserProfile นั้น
        cart, created = Cart.objects.get_or_create(cart=user_profile)
        
        cart_detail = Detailcart.objects.filter(carts=cart)
        count = sum(detail.amount for detail in cart_detail)
        
        context = {'count': count, 'cart': cart_detail}
        return render(req, 'productweb/cart.html', context)
    except UserProfile.DoesNotExist:
        pass
@login_required
def add_cart(req, id):
    products = ItemImage.objects.filter(item=id)
    
    try:
        user_profile = UserProfile.objects.get(user=req.user)
        cart, created = Cart.objects.get_or_create(cart=user_profile)
        product_instance = products.first()
        
        cart_detail = Detailcart.objects.create(
            itemImages=product_instance,
            carts=cart,
            amount=1,
        )
        cart_detail.save()
        return HttpResponseRedirect(reverse('cart'))
    except UserProfile.DoesNotExist:
        pass

def add_products(request, product_id):
    product_instance = Item.objects.get(id=product_id)
    context = {'product': product_instance}
    return render(request, 'productweb/add_products.html', context)
    
def contag(req):
    return render(req,'productweb/contag.html')

def payments(req):
    return render(req,'payment/payments.html')

def order(request):
    return render(request, 'order/preorder.html')

def delete_product(request, product_id):
    cart_item = get_object_or_404(Detailcart, id=product_id)
    if request.method == 'POST':
        cart_item.delete()
        return redirect('cart') 
    return render(request, 'productweb/delete_product.html', {'product': cart_item})

