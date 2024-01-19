# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

from admin.admin_auth.models import User
from admin.dishmanage.models import Dish


class Foodcategory(models.Model):
    name = models.CharField(unique=True, max_length=100)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='media/admin/img/', blank=True, null=True)

    class Meta:
        app_label = 'admin.foodmanage'

        managed = False
        db_table = 'foodcategory'


class Food(models.Model):
    name = models.CharField(unique=True, max_length=100)
    description = models.TextField(blank=True, null=True)
    image = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        app_label = 'admin.foodmanage'

        managed = False
        db_table = 'food'


class FoodDish(models.Model):
    food = models.OneToOneField(Food, models.DO_NOTHING, db_column='Food_id',
                                primary_key=True)  # Field name made lowercase. The composite primary key (Food_id, Dish_id) found, that is not supported. The first column is selected.
    dish = models.ForeignKey(Dish, models.DO_NOTHING, db_column='Dish_id')  # Field name made lowercase.
    value = models.FloatField()
    count = models.IntegerField()

    class Meta:
        app_label = 'admin.foodmanage'

        managed = False
        db_table = 'food_dish'
        unique_together = (('food', 'dish'),)


class FoodFoodcategory(models.Model):
    food = models.OneToOneField(Food, models.DO_NOTHING, db_column='Food_id',
                                primary_key=True)  # Field name made lowercase. The composite primary key (Food_id, FoodCategory_id) found, that is not supported. The first column is selected.
    foodcategory = models.ForeignKey(Foodcategory, models.DO_NOTHING,
                                     db_column='FoodCategory_id')  # Field name made lowercase.

    class Meta:
        app_label = 'admin.foodmanage'

        managed = False
        db_table = 'food_foodcategory'
        unique_together = (('food', 'foodcategory'),)
