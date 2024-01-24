from django.urls import path, include

from .views import *
urlpatterns = [
        path('', index, name='foodarticlemanage'),
        path('edit/', edit_article, name='editfoodarticle')
]
