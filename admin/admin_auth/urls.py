from django.urls import path
from .views import *

urlpatterns = [
    path('', login, name='auth'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
]