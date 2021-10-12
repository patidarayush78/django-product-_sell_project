from django.shortcuts import render,redirect
from .forms import addotherga, enquiryform
from .models import orderog, otherga, user_enquiry1
from django.contrib.auth.models import User
from random import randint
# Create your views here.


def productdetail(request,id):
    od=id
    displaymore=otherga.objects.get(pk=id) 
    n=randint(1,2)
    rand=otherga.objects.get(pk=n)


    n1=randint(1,2)
    rand1=otherga.objects.get(pk=n1)
    
    n2=randint(1,2)
    rand2=otherga.objects.get(pk=n2)

    n3=randint(1,2)
    rand3=otherga.objects.get(pk=n3)

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
            order=otherga.objects.get(pk=id) 
            todos=orderog.objects.filter(user=request.user)
            for i in todos:

                ap=i.user

   
            us=ap
            bn=order.brand_name
            pr=order.price
            cp=order.coverphoto
            reg=orderog(brand=bn,priceo=pr,coverphotoo=cp,user=us)
            reg.save()
            
            
    else:
        enfm=enquiryform()
    return render(request,'main/productdetail.html',{'dsm':displaymore,'enqform':enfm,'dsm1':od,'randm':rand,'randm1':rand1,'randm2':rand2,'randm3':rand3})

def additem(request):
    return render(request,'main/additem.html')

def othergagallery(request):
    mg=otherga.objects.all()
    return render(request,'main/othergagallery.html',{'mg1':mg})

def update(request):
    upd=otherga.objects.all()
    return render(request,'main/update.html',{'up':upd})

def updatepage(request,id):
    if request.method=='POST':
        pi=otherga.objects.get(pk=id)
        fm=addotherga(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()

    else:
        pi=otherga.objects.get(pk=id)
        fm=addotherga(instance=pi)
    return render(request,'main/updatepage.html',{'up':fm,'pi':pi})


def othergapage(request):
       
    if request.method=='POST':
        fm=addotherga(request.POST,request.FILES)
        if fm.is_valid():
            br=fm.cleaned_data['brand_name']
            pr=fm.cleaned_data['price']
            orp=fm.cleaned_data['original_price']
           
            ds=fm.cleaned_data['description']
            cimg=fm.cleaned_data['coverphoto']
            pho=fm.cleaned_data['photo']
          
            reg=otherga(brand_name=br,price=pr,original_price=orp,description=ds,coverphoto=cimg,photo=pho)
            reg.save()
            
            
                   
                
               
    else:
        fm=addotherga()
     
    return render(request,'main/addotherga.html',{'othergaform':fm})


def userordervi(request,id):
    order=otherga.objects.get(pk=id) 
    todos=orderog.objects.filter(user=request.user)
    for i in todos:

        ap=i.user

   
    us=ap
    bn=order.brand_name
    pr=order.price
    cp=order.coverphoto
    reg=orderog(brand=bn,priceo=pr,coverphotoo=cp,user=us)
    reg.save()
    
    return redirect('home')

def othergacart(request):
    if request.user.is_authenticated:
        todos=orderog.objects.filter(user=request.user)
        return render(request,'main/othergacart.html',{'todo':todos})
    else:
        return render(request,'emptycart.html')
    # if User:
    #     user=User.objects.get()
    #     return render(request,'othergacart.html',{'cart':user})
    # else:
    #     return redirect('home')