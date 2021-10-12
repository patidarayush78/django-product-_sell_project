from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
from django.forms.widgets import Widget
from .models import otpemailmodel



class UserRegisterForm1(UserCreationForm):
	email = forms.EmailField(label='email')
	# first_name=forms.IntegerField(label='otp')
	username = forms.CharField(max_length = 20,)
	password1 = forms.CharField(max_length =20,label='password')
	password2 = forms.CharField(max_length = 20,label='re-password')
	class Meta:
		
		model = User
		fields = ['username', 'email', 'password1', 'password2']
		labels = {
            'username': (''),
            'email': (''),
            'password1': (''),
            'password2': (''),
            'first_name': (''),


        }
		

class emailform(forms.ModelForm):
	class Meta:
		model= otpemailmodel
		fields=['email1']

	     
		 