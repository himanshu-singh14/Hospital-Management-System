from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('register/', register, name='register'),
    path('user_login/', userLogin, name='user-login'),
    path('user_logout/', userLogout, name='user-logout'),
]