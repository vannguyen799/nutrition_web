from django.urls import path
from .views import *

urlpatterns = [
    path('', login, name='admin_auth'),
    path('login/', login, name='admin_login'),
    path('logout/', logout, name='admin_logout'),
]