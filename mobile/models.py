from django.db import models

# Create your models here.
class mobile(models.Model):
    brand_name=models.CharField(max_length=20)
    price=models.IntegerField()
    original_price=models.IntegerField()
    ram=models.IntegerField()
    rom=models.IntegerField()
    primary_camera=models.IntegerField()
    secondary_camera=models.IntegerField()
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
   
