from django.db import models

from admin.nutrientmanage.models import Nutrient


# Create your models here.

class Dishcategory(models.Model):
    name = models.CharField(unique=True, max_length=100)
    description = models.TextField(blank=True, null=True)
    dishcategory = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        app_label = 'admin.foodmanage'
        managed = False
        db_table = 'dishcategory'


class Dish(models.Model):
    name = models.CharField(unique=True, max_length=100)
    image = models.CharField(max_length=200)
    kcal = models.IntegerField()
    refuse_rate = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    dishcategory = models.ForeignKey(Dishcategory, models.DO_NOTHING,
                                     db_column='DishCategory_id')  # Field name made lowercase.

    class Meta:
        app_label = 'admin.foodmanage'
        managed = False
        db_table = 'dish'


class DishNutrient(models.Model):
    dish = models.OneToOneField(Dish, models.DO_NOTHING, db_column='Dish_id',
                                primary_key=True)  # Field name made lowercase. The composite primary key (Dish_id, Nutrient_id) found, that is not supported. The first column is selected.
    nutrient = models.ForeignKey(Nutrient, models.DO_NOTHING, db_column='Nutrient_id')  # Field name made lowercase.
    value = models.FloatField(blank=True, null=True)

    class Meta:
        app_label = 'admin.foodmanage'
        managed = False
        db_table = 'dish_nutrient'
        unique_together = (('dish', 'nutrient'),)
