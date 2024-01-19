"""
URL configuration for nutrition_web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from .views import *
from django.urls import path, include

urlpatterns = [
        path('', index, name='admin_foodmanage'),
        path('add/', add_food, name='admin_addfood'),
        path('edit/', update_food, name='admin_editfood'''),
        path('delete/', delete_food, name='admin_deletefood'''),
        path('category/', manage_food_categories, name='admin_foodcategory'),
        path('category/add/', add_food_category, name='admin_addfoodcategory'),
        path('category/edit/', edit_food_category, name='admin_editfoodcategory'),
        path('category/delete/', delete_food_category, name='admin_deletefoodcategory')
]
