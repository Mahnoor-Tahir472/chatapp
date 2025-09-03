"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from chatapp.views import SignupAPI , LogInAPI , LogoutAPI, CheckLogin, GetAllUsers, CreatePrivateRoom, PostMessage, GetMessage, NewSignupAPI, NewLoginAPI, GetAllUser, NewPrivateRoom

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', SignupAPI.as_view(),name='Signup'), 
    path('login/', LogInAPI.as_view() , name='login'),
    path('logout/', LogoutAPI.as_view() , name='logout'),
    path('checklogin/', CheckLogin.as_view() , name='checklogin'),
    path('getallusers/', GetAllUsers.as_view() , name='getallusers'),
    path('createroom/', CreatePrivateRoom.as_view() , name='createprivateroom'),
    path('sendmessage/', PostMessage.as_view() , name='sendmessage'),
    path('getmessage/<int:roomid>/', GetMessage.as_view() , name='getmessage'),
    path('newsignup/', NewSignupAPI.as_view(),name='NewSignup'), 
    path('newlogin/', NewLoginAPI.as_view(),name='NewLogin'), 
    path('getalluser/', GetAllUser.as_view() , name='getalluser'),
    path('newroom/', NewPrivateRoom.as_view() , name='newprivateroom'),
    
]
