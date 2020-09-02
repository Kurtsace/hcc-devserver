from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views import generic

# Create your views here.


#Login View
class Login(LoginView):
    
    #Template 
    template_name = 'accounts/login.html'
    
#Log out view 
class Logout(LogoutView):
    
    #Redirect
    next_page = '/'
    
#Registration page 
class RegisterUser(generic.CreateView):
    
    #Model
    model = User 
    
    #Template 
    template_name = 'accounts/register.html'

    #Form
    form_class = UserCreationForm
    
    #Redirect
    success_url = '/'