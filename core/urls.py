from django.urls import path
from .views import homepage, profile, user_login, registr, news, advice

urlpatterns = [
    path('', homepage, name='homepage'),
    path('profile/', profile, name='profile'),
    path('register/', registr, name='register'),
    path('news/', news, name='news'),
    #path('<int:id>/', post, name='post'),
    path('advice/', advice, name='advice'),
    path('login/', user_login, name='login'),
  
        
]