from django.urls import path
from .views import homepage, profile, login, registr, news, advice

urlpatterns = [
    path('', homepage, name='homepage'),
    path('profile/', profile, name='profile'),
    path('register/', registr, name='register'),
    
    path('login/', login, name='login'),
    path('news/', news, name='news'),
    path('advice/', advice, name='advice'),

]