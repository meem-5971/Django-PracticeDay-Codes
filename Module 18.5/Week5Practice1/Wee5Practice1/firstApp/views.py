from django.shortcuts import render,redirect
from .forms import RegisterForm,ChangeUserData
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request,'./home.html')

def signup(request):
    if request.method == 'POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            messages.success(request,"Account Created successfully")
            form.save()
            print(form.cleaned_data)

    else:
        form=RegisterForm()

    return render(request,'./signup.html',{'form':form})

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            login_form=AuthenticationForm(request=request, data=request.POST)
            if login_form.is_valid():
                name=login_form.cleaned_data['username']
                userpass=login_form.cleaned_data['password']
                user=authenticate(username=name,password=userpass)
                # messages.success(request,"Logged in successfully")
                if user is not None:
                    login(request,user)
                    return redirect('profile')
        else:
            login_form=AuthenticationForm()
        return render(request,'login.html',{'form':login_form})
    else:
        return redirect('profile')
    

# @login_required   
def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            update_form=ChangeUserData(request.POST,instance=request.user)
            if update_form.is_valid():
                # messages.success("Profile updated successfully")
                update_form.save()
                print(update_form.cleaned_data)
        else:
            update_form=ChangeUserData()
        return render(request,'./profile.html',{'form':update_form})
    else:
        # messages.warning("No account")
        return redirect('signup')
    

# @login_required      
def pass_change(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form=PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user)
                # messages.success("Password changed successfully")
                return redirect('profile')
        else:
            form=PasswordChangeForm(user=request.user)
        return render(request,'./passchange.html',{'form':form})
    else:
        return redirect('login')
    
# @login_required     
def pass_change2(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form=SetPasswordForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                # update_session_auth_hash(request,form.user)
                # messages.success("Password changed successfully without old password" )
                return redirect('profile')
        else:
            form=SetPasswordForm(user=request.user)
        return render(request,'./passchange.html',{'form':form})
    else:
        return redirect('login')  

# @login_required     
def user_logout(request):
    logout(request)
    return redirect('login')








    