from django.shortcuts import render
from .forms import addmobile, enquiryform
from .models import mobile, user_enquiry1
# Create your views here.


def productdetail(request,id):
    displaymore=mobile.objects.get(pk=id) 
    brand=displaymore.brand_name
    price=displaymore.price

    if request.method=='POST':
        enfm=enquiryform(request.POST)
        if enfm.is_valid():
            pc=brand
            sc=price
            br=enfm.cleaned_data['full_name']
            pr=enfm.cleaned_data['phone_no']
            orp=enfm.cleaned_data['district']
            rm=enfm.cleaned_data['address']
            ro=enfm.cleaned_data['message']
           
           
          
            reg=user_enquiry1(full_name=br,phone_no=pr,district=orp,address=rm,message=ro,brand_name=pc,price=sc)
            reg.save()
            
    else:
        enfm=enquiryform()
    return render(request,'main/productdetail.html',{'dsm':displaymore,'enqform':enfm})

def additem(request):
    return render(request,'main/additem.html')

def mobilegallery(request):
    mg=mobile.objects.all()
    return render(request,'main/mobilegallery.html',{'mg1':mg})

def mobilepage(request):
       
    if request.method=='POST':
        fm=addmobile(request.POST,request.FILES)
        if fm.is_valid():
            br=fm.cleaned_data['brand_name']
            pr=fm.cleaned_data['price']
            orp=fm.cleaned_data['original_price']
            rm=fm.cleaned_data['ram']
            ro=fm.cleaned_data['rom']
            pc=fm.cleaned_data['primary_camera']
            sc=fm.cleaned_data['secondary_camera']
            ds=fm.cleaned_data['description']
            cimg=fm.cleaned_data['coverphoto']
            pho=fm.cleaned_data['photo']
          
            reg=mobile(brand_name=br,price=pr,original_price=orp,ram=rm,rom=ro,primary_camera=pc,secondary_camera=sc,description=ds,coverphoto=cimg,photo=pho)
            reg.save()
            
                   
                
               
    else:
        fm=addmobile()
     
    return render(request,'main/addmobile.html',{'mobileform':fm})