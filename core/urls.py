from django.urls import path
from .views import homepage, profile, user_login, registr, news, advice, logout, user_delete


urlpatterns = [
    path('', homepage, name='homepage'),
    path('profile/', profile, name='profile'),
    path('register/', registr, name='register'),
    path('news/', news, name='news'),
    path('advice/', advice, name='advice'),
    path('login/', user_login, name='login'),
    path("logout",logout,name="logout"),
    path('delete/<int:id>', user_delete, name='delete'),
]
