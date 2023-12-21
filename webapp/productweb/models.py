from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    title = models.CharField(max_length=50)
    size = models.CharField(max_length=500)
    description = models.TextField(max_length=255, default='No description')
    material = models.CharField(max_length=50, default='No description')
    price = models.CharField(max_length=50)
    is_available = models.BooleanField(default=True, blank=True, null=True)

class ItemImage(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images', null=True, blank=True)

