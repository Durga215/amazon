from django.db import models

# Create your models here.
class data1(models.Model):
    product = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
