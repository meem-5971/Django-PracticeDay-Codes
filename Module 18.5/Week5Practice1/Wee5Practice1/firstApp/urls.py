from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('passchange/',views.pass_change,name='passchange'),
    path('passchange2/',views.pass_change2,name='passchange2'),
    path('',views.home,name='home'),
]