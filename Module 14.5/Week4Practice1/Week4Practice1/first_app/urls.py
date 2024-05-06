from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('model/',views.modelview,name="model"),
    path('form/',views.formview,name="form"),
]