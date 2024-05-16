from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm,UserCreationForm
from django import forms

class RegisterForm(UserCreationForm):
    # username = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    class Meta:
        model=User
        fields=['username','email', 'first_name', 'last_name']

class ChangeUserData(UserChangeForm):
    # username = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    class Meta:
        model=User
        fields=['username','email', 'first_name', 'last_name']