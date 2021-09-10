from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


def homepage(request):
    return render(request, 'core/index.html')

def profile(request):
    user = request.user
    profile_object = user.profile
    return render(request, 'core/profile.html', {'profile': profile_object})

def login(request):
    user = request.user
    login_object = user.profile
    return render(request, 'core/login.html', {'login': login_object})



def news(request):
   return render(request, 'core/news.html')

def advice(request):
   return render(request, 'core/advice.html')

def registr(request):
    form = UserCreationForm(request.POST or None) 
    msg = "йцукен"
    if form.is_valid():
        form.save() 
        return redirect('profile')                        
    return render(request, 'core/register.html', {'form': form})