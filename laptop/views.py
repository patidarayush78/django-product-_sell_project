from django.shortcuts import render
from .forms import addlap, enquiryform
from .models import laptop, orderla, user_enquiry1
from random import randint
# Create your views here.


def laptopdetail(request,id):
    od=id
    displaymore=laptop.objects.get(pk=id) 
    n=randint(1,2)
    rand=laptop.objects.get(pk=n)


    n1=randint(1,2)
    rand1=laptop.objects.get(pk=n1)
    
    n2=randint(1,2)
    rand2=laptop.objects.get(pk=n2)

    n3=randint(1,2)
    rand3=laptop.objects.get(pk=n3)

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
            ord=laptop.objects.get(pk=id) 
            todos=orderla.objects.filter(user=request.user)
            for i in todos:

                ap=i.user

   
            us=ap
            bn=ord.brand_name
            pr=ord.price
            cp=ord.coverphoto
            reg=orderla(brand=bn,priceo=pr,coverphotoo=cp,user=us)
            reg.save()
            
            
    else:
        enfm=enquiryform()
    return render(request,'main/productdetaillap.html',{'dsl':displaymore,'enqforml':enfm,'dsm1':od,'randm':rand,'randm1':rand1,'randm2':rand2,'randm3':rand3})

def additemlap(request):
    return render(request,'main/additemlap.html')

def lapgallery(request):
    mg=laptop.objects.all()
    return render(request,'main/lapgallery.html',{'mgl':mg})

def updates(request):
    
    upd=laptop.objects.all()
    return render(request,'main/updates.html',{'up':upd})

def updatepage(request,id):
    if request.method=='POST':
        pi=laptop.objects.get(pk=id)
        fm=addlap(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()

    else:
        pi=laptop.objects.get(pk=id)
        fm=addlap(instance=pi)
    return render(request,'main/updatepage.html',{'up':fm,'pi':pi})


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


def laptopcart(request):
    if request.user.is_authenticated:
       todos=orderla.objects.filter(user=request.user)  
       return render(request,'main/laptopcart.html',{'todo':todos})
    else:
        return render(request,'emptycart.html')