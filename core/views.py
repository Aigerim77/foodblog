from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from .models import Profile, News, Advice



def homepage(request):
    return render(request, 'core/index.html')

def profile(request):
    user = request.user
    profile_object = user.profile
    return render(request, 'core/profile.html', {'profile': profile_object})


def registr(request):
    form = UserCreationForm(request.POST or None) 
    User.profile = property(lambda u: Profile.objects.get_or_create(user=u)[0])
    if form.is_valid():
        form.save()
        
        return redirect('profile')                        
    return render(request, 'registration/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('profile')
                #else:
                 #   return HttpResponse('Disabled account')
            #else:
             #   return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})


def news(request):
    news_objects = News.objects.all()
    return render(request, 'core/news.html', {'news_objects': news_objects})

def post(request, id):
    post_object = News.objects.get(id=id)
    return render(request, 'core/post.html', {'post_object': post_object})

def advice(request):
    advice_object = Advice.objects.all()
    return render(request, 'core/advice.html', {'advice_object': advice_object})




