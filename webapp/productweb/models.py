from django.db import models

# Create your models here.
class item(models.Model):
    title = models.CharField(max_length=50)
    size = models.CharField(max_length=50)