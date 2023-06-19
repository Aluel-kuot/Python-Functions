
from django.db import models
class Customer (models.Model):
    customer_id = models.PositiveIntegerField
    first_name = models.CharField(max_length=32, default='')
    second_name = models.CharField(max_length=32,default='')
    email= models.EmailField(default='')
# Create your models here.
