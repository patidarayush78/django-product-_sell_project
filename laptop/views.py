from django.shortcuts import render
from .forms import addlap, enquiryform
from .models import laptop, user_enquiry1
# Create your views here.


def laptopdetail(request,id):
    displaymore=laptop.objects.get(pk=id) 
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
    return render(request,'main/productdetaillap.html',{'dsl':displaymore,'enqforml':enfm})

def additemlap(request):
    return render(request,'main/additemlap.html')

def lapgallery(request):
    mg=laptop.objects.all()
    return render(request,'main/lapgallery.html',{'mgl':mg})

def lappage(request):
       
    if request.method=='POST':
        fm=addlap(request.POST,request.FILES)
        if fm.is_valid():
            br=fm.cleaned_data['brand_name']
            pr=fm.cleaned_data['price']
            orp=fm.cleaned_data['original_price']
            rm=fm.cleaned_data['ram']
            ro=fm.cleaned_data['ssd']
            pc=fm.cleaned_data['hdd']
            sc=fm.cleaned_data['pgeneration']
            scs=fm.cleaned_data['screensize']
            proces=fm.cleaned_data['processor']
            ds=fm.cleaned_data['description']
            cimg=fm.cleaned_data['coverphoto']
            pho=fm.cleaned_data['photo']
          
            reg=laptop(brand_name=br,price=pr,original_price=orp,ram=rm,ssd=ro,hdd=pc,pgeneration=sc,screensize=scs,processor=proces,description=ds,coverphoto=cimg,photo=pho)
            reg.save()
            
                   
                
               
    else:
        fm=addlap()
     
    return render(request,'main/addlap.html',{'lapform':fm})