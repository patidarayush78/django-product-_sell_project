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


    path('laptop/<int:id>/',lv.laptopdetail,name='hellooo'),
    path('additemlap/',lv.additemlap,name='lapadditem'),
    path('addlap/',lv.lappage,name='addlap'),
    path('lapgallery/',lv.lapgallery,name='lapgallery'),


] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
