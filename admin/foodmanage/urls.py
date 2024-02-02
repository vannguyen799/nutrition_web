from .views import *
from django.urls import path

urlpatterns = [
        path('', index, name='foodmanage'),
        path('add/', add_food, name='addfood'),
        path('edit/', update_food, name='editfood'),
        path('delete/', delete_food, name='deletefood'),
        path('category/', manage_food_categories, name='foodcategorymanage'),
        path('category/add/', add_food_category, name='addfoodcategory'),
        path('category/edit/', edit_food_category, name='editfoodcategory'),
        path('category/delete/', delete_food_category, name='deletefoodcategory')
]
