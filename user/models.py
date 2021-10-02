from django.db import models

# Create your models here.
class otpemailmodel(models.Model):    
    otp=models.IntegerField()
    email1=models.CharField(max_length=50)