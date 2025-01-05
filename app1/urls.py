
from django.urls import path,include
from  .views import *

urlpatterns = [
    path('',home, name='home'),
    path("register/",register,name="register"),
    path("login/",login,name="login"),
    path('cpregister/',cpregister,name='cpregister'),
    path('logout/',logout,name='logout'),
    path('logout/',logout,name='logout'),
    path('sendotp/',sendotp,name='sendotp'),
    path('otpverify/',otpverify,name='otpverify'),
    path('password/',password,name='password'),
    
]