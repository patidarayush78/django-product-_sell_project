"""jugal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from mobile import views as mv

from django.conf import settings
from django.conf.urls.static import static
from user import views as user_view
from laptop import views as lv
from color_fan import views as cfv
from lighting import views as liv
from other_gadget import views as ogv
from kitchen import views as ktv
from django.views.static import serve
from django.conf.urls import url

from django.contrib.auth import views as auth


urlpatterns = [
    path('admin/', admin.site.urls),
   path('signup/', user_view.signup, name ='signup'),
    path('home/', user_view.home, name ='home'),
    path('current/', user_view.todo, name ='current'),
    path('email/', user_view.email, name ='email'),
    path('logout/', user_view.logout, name ='logout'),
    path('login/', user_view.loginuser, name ='login'),
	
    
    
    
    path('<int:id>/',mv.productdetail,name='mobiledetail'),
    path('additem/',mv.additem,name='additem'),
    path('addmobile/',mv.mobilepage),
    path('mobilegallery/',mv.mobilegallery,name='mobilegallery'),
   
    path('mobilecart/',mv.mobilecart,name='mobilecart'),


    path('laptop/<int:id>/',lv.laptopdetail,name='hellooo'),
    path('additemlap/',lv.additemlap,name='lapadditem'),
    path('addlap/',lv.lappage,name='addlap'),
    path('lapgallery/',lv.lapgallery,name='lapgallery'),
    path('laptopcart/',lv.laptopcart,name='laptopcart'),



    path('colorfan/<int:id>/',cfv.productdetail,name='colorfandetail'),
    path('additemcolor/',cfv.additem,name='additemcolor'),
    path('addcolorfan/',cfv.colorfanpage,name='addcolorfan'),
    path('colorfangallery/',cfv.colorfangallery,name='colorfangallery'),
    
    path('colorfancart/',cfv.colorfancart,name='colorfancart'),



    path('lighting/<int:id>/',liv.productdetail,name='lightingdetail'),
    path('additemlighting/',liv.additem,name='additemlighting'),
    path('addlighting/',liv.lightingpage,name='addlighting'),
    path('lightinggallery/',liv.lightinggallery,name='lightinggallery'),
    
    path('lightingcart/',liv.lightingcart,name='lightingcart'),


    path('kitchen/<int:id>/',ktv.productdetail,name='kitchendetail'),
    path('additemkitchen/',ktv.additem,name='additemkitchen'),
    path('addkitchen/',ktv.kitchenpage,name='addkitchen'),
    path('kitchengallery/',ktv.kitchengallery,name='kitchengallery'),
    
    path('kitchencart/',ktv.kitchencart,name='kitchencart'),


    path('otherga/<int:id>/',ogv.productdetail,name='othergadetail'),
    path('additemotherga/',ogv.additem,name='additemotherga'),
    path('addotherga/',ogv.othergapage,name='addotherga'),
    path('othergagallery/',ogv.othergagallery,name='othergagallery'),
    
    path('othergacart/',ogv.othergacart,name='othergacart'),



    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
     



] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
