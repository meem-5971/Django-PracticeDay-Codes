from django.urls import path,include
from .views import UserRegistrationView,UserLoginView,UserBankAccountUpdateView,PassChangeView
from . import views

urlpatterns = [
    path('register/',UserRegistrationView.as_view(),name='register'),
    path('login/',UserLoginView.as_view(),name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('profile/', UserBankAccountUpdateView.as_view(), name='profile' ),
    path('profile/pass_change/',PassChangeView.as_view() , name='pass_change'),

]