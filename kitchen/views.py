from django.shortcuts import render,redirect
from .forms import addkitchen, enquiryform
from .models import orderk, kitchen, kitchen, user_enquiry1
from django.contrib.auth.models import User
from random import randint
# Create your views here.


def productdetail(request,id):
    od=id
    displaymore=kitchen.objects.get(pk=id) 
    n=randint(1,2)
    rand=kitchen.objects.get(pk=n)


    n1=randint(1,2)
    rand1=kitchen.objects.get(pk=n1)
    
    n2=randint(1,2)
    rand2=kitchen.objects.get(pk=n2)

    n3=randint(1,2)
    rand3=kitchen.objects.get(pk=n3)

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
           
            print('helloooo')
          
            reg=user_enquiry1(full_name=br,phone_no=pr,district=orp,address=rm,message=ro,brand_name=pc,price=sc)
            reg.save()
            order=kitchen.objects.get(pk=id) 
            todos=orderk.objects.filter(user=request.user)
            for i in todos:

                ap=i.user

   
            us=ap
            bn=order.brand_name
            pr=order.price
            cp=order.coverphoto
            reg=orderk(brand=bn,priceo=pr,coverphotoo=cp,user=us)
            reg.save()
            
            
    else:
        enfm=enquiryform()
    return render(request,'main/productdetail.html',{'dsm':displaymore,'enqform':enfm,'dsm1':od,'randm':rand,'randm1':rand1,'randm2':rand2,'randm3':rand3})

def additem(request):
    return render(request,'main/additem.html')

def kitchengallery(request):
    mg=kitchen.objects.all()
    return render(request,'main/kitchengallery.html',{'mg1':mg})

def update(request):
    upd=kitchen.objects.all()
    return render(request,'main/update.html',{'up':upd})

def updatepage(request,id):
    if request.method=='POST':
        pi=kitchen.objects.get(pk=id)
        fm=addkitchen(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()

    else:
        pi=kitchen.objects.get(pk=id)
        fm=addkitchen(instance=pi)
    return render(request,'main/updatepage.html',{'up':fm,'pi':pi})


def kitchenpage(request):
       
    if request.method=='POST':
        fm=addkitchen(request.POST,request.FILES)
        if fm.is_valid():
            br=fm.cleaned_data['brand_name']
            pr=fm.cleaned_data['price']
            orp=fm.cleaned_data['original_price']
           
            ds=fm.cleaned_data['description']
            cimg=fm.cleaned_data['coverphoto']
            pho=fm.cleaned_data['photo']
          
            reg=kitchen(brand_name=br,price=pr,original_price=orp,description=ds,coverphoto=cimg,photo=pho)
            reg.save()
            
            
                   
                
               
    else:
        fm=addkitchen()
     
    return render(request,'main/addkitchen.html',{'kitchenform':fm})


def userordervi(request,id):
    order=kitchen.objects.get(pk=id) 
    todos=orderk.objects.filter(user=request.user)
    for i in todos:

        ap=i.user

   
    us=ap
    bn=order.brand_name
    pr=order.price
    cp=order.coverphoto
    reg=orderk(brand=bn,priceo=pr,coverphotoo=cp,user=us)
    reg.save()
    
    return redirect('home')

def kitchencart(request):
    
    if request.user.is_authenticated:
        todos=orderk.objects.filter(user=request.user)
        return render(request,'main/kitchencart.html',{'todo':todos})
    else:
        return render(request,'emptycart.html')
    
    # if User:
    #     user=User.objects.get()
    #     return render(request,'kitchencart.html',{'cart':user})
    # else:
    #     return redirect('home') else:
        