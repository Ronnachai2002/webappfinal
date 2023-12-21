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
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('products/', products, name='products'),
    path('product/<int:item_id>/', product, name='product'),
    path('productweb/product/<int:item_id>/', product, name='product'),
    path('contag/', contag, name='contag'),
    path('payments/', payments, name='payments'),
    path('order/', order, name='order'),
    path('add_product/', add_product, name='add_product'),
    path('delete_product/<int:product_id>/', delete_product, name='delete_product'),
    path('add_products/<int:product_id>/', views.add_products, name='add_products'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)