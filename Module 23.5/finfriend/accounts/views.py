from django.shortcuts import render,redirect
from django.views.generic import FormView,View
from django.contrib.auth.views import LoginView,PasswordChangeView
from .forms import UserRegistrationForm,UserUpdateForm
from django.contrib.auth import login,logout
from django.urls import reverse_lazy
from . import forms
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string

# Create your views here.
def send_pass_change_email(user,subject,template):
        message=render_to_string(template,{
            'user':user,
            
        })
        
        send_email =EmailMultiAlternatives(subject,'',to=[user.email])
        send_email.attach_alternative(message,'text/html')
        send_email.send()

class UserRegistrationView(FormView):
    template_name='accounts/user_registration.html'
    form_class=UserRegistrationForm
    success_url=reverse_lazy('register')

    def form_valid(self,form):
        user=form.save()
        login(self.request,user)
        return super().form_valid(form)
    
class UserLoginView(LoginView):
    template_name='accounts/user_login.html'
    def get_success_url(self):
        return reverse_lazy('home')
    
def user_logout(request):
    logout(request)
    return redirect('home')

class UserBankAccountUpdateView(View):
    template_name = 'accounts/profile.html'

    def get(self, request):
        form = UserUpdateForm(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the user's profile page
        return render(request, self.template_name, {'form': form})


class PassChangeView(PasswordChangeView):
    template_name = 'accounts/pass_change.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        messages.success(self.request, 'Password Updated Successfully')
        send_pass_change_email(self.request.user,"Password Change Warning","accounts/pass_change_email.html")
        return super().form_valid(form)
        
