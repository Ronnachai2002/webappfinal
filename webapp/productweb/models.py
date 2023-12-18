from django.db import models

class Item(models.Model):
    title = models.CharField(max_length=50)
    size = models.CharField(max_length=500)
    description = models.TextField(default='No description')
    material = models.CharField(max_length=50, default='No description')
    price = models.CharField(max_length=50)

class ItemImage(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images', null=True, blank=True)