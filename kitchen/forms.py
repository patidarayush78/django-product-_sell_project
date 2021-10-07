
from django import forms
from django.forms import fields, widgets
from .models import kitchen, user_enquiry1

class addkitchen(forms.ModelForm):

    class Meta:
          
        model= kitchen
        fields="__all__"

class enquiryform(forms.ModelForm):
    class Meta:
        model=user_enquiry1
        fields='__all__'
        exclude = ['brand_name','price']
        labels = {
            'full_name': (''),
            'phone_no': (''),
            'district': (''),
            'address': (''),
            'message': (''),


        }

        help_text = {
            'full_name': 'heyyy'
        }
        error_messages={'full_name':{'Required':'you have to'}}
        widgets={'full_name':forms.TextInput(attrs={'class':'myclass','placeholder':'name'}),
        'phone_no':forms.TextInput(attrs={'class':'myclass','placeholder':'phone no.'}),
        'district':forms.TextInput(attrs={'class':'myclass','placeholder':'district'}),
        'address':forms.TextInput(attrs={'class':'myclass','placeholder':'address'}),
        'message':forms.TextInput(attrs={'class':'myclass','placeholder':'leave a message for seller'})}