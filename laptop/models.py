from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class laptop(models.Model):
    brand_name=models.CharField(max_length=20)
    price=models.IntegerField()
    original_price=models.IntegerField()
    ram=models.IntegerField()
    ssd=models.IntegerField()
    hdd=models.IntegerField()
    pgeneration=models.IntegerField()
    screensize=models.IntegerField()
    processor=models.CharField(max_length=20)
    description=models.CharField(max_length=300)
    coverphoto=models.ImageField()
    photo=models.ImageField()

class user_enquiry(models.Model):
    
    
    full_name=models.CharField(max_length=50)
   
    phone_no=models.IntegerField()
    district=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    
    message=models.CharField(max_length=200)
    name=models.CharField(max_length=200)
    money=models.IntegerField()

class user_enquiry1(models.Model):
    brand_name=models.CharField(max_length=100)
    price=models.IntegerField()
    
    
    full_name=models.CharField(max_length=50)
   
    phone_no=models.IntegerField()
    district=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    
    message=models.CharField(max_length=200)
   
class orderla(models.Model):
    brand=models.CharField(max_length=20,default='')
    priceo=models.IntegerField()
    coverphotoo=models.ImageField()
    user=models.ForeignKey(User,null=True,default=1,on_delete=models.SET_NULL)
    dateorder=models.DateTimeField(null=True,default=None)