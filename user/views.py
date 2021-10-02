from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from .forms import UserRegisterForm1,emailform
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from .models import otpemailmodel

from django.conf import settings
from random import randint

def email(request):

    
    
    if request.method=='POST':
        
        fm=emailform(request.POST)
       
        
        if fm.is_valid():
            n=randint(1000,2000)
            print(n)
           
            em =fm.cleaned_data['email1']
            otpm=otpemailmodel(otp=n,email1=em)
            otpm.save()
            
            
            
            send_mail(
                n,
                'hello',
                settings.EMAIL_HOST_USER,
                [em],
                fail_silently=False,
                      )
            print(em)
            
        return redirect('signup')
    else:
        
        fm=emailform()
  
   
    return render(request,'email.html',{'form':fm})



#################### index #######################################
def signup(request):
   
    if request.method=='GET':
        
	    return render(request, 'signup.html', {'form':UserRegisterForm1})
    else:
        stud=otpemailmodel.objects.all()
        for i in stud:
            email1c=i.email1
            otpc=i.otp
        
        if (request.POST['password1']==request.POST['password2']) and (request.POST['email']==email1c) and int(request.POST['first_name'])==otpc :
            try:
                user=User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('home')
            except IntegrityError:
                return render(request,'signup.html',{'form':UserRegisterForm1,'error':'email alraedy taken'})
            
        else:
            return render(request,'signup.html',{'form':UserRegisterForm1,'error':'password nnot match'})
            
    

            
def todo(request):

    return render(request,'current.html')

def home(request):

    return render(request,'home.html')

def logout(request):
    if request.method =='POST':
        auth_logout(request)
        return redirect('home')

def loginuser(request):
    if request.method=='GET':
        
	    return render(request, 'login.html', {'form':AuthenticationForm()})
    else:
        user=authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if user is None:
             return render(request,'login.html',{'form':AuthenticationForm(),'error':'password nnot match'})
            
        else:
            login(request,user)
            return redirect('home')
