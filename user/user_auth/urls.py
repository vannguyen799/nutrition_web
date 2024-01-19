from .views import *
from django.urls import path

urlpatterns = [
    path('login/', login, name='user_login'),
    path('logout/', logout, name='user_logout'),
    path('register/', register, name='user_register')
]
