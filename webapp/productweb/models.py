from django.db import models

class item(models.Model):
    title = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    description = models.CharField(max_length=255, default='No description')
    matter = models.CharField(max_length=50, default='No description')
    image = models.ImageField(upload_to='product_images', null=True, blank=True)
