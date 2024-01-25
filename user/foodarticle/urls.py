from .views import *
from django.urls import path

urlpatterns = [
    path('', index, name="foodarticle"),
    path('post/<slug:slug_id>/', article_view, name="articleview")
]
