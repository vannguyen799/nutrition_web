from django.db import models


# Create your models here.


class Nutrientcategory(models.Model):
    name = models.CharField(unique=True, max_length=100)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='admin/img/', blank=True, null=True)

    class Meta:
        app_label = 'admin.nuritentmanage'
        managed = False
        db_table = 'NutrientCategory'


class Nutrient(models.Model):
    name = models.CharField(unique=True, max_length=100)
    unit = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    nutrientcategory = models.ForeignKey(Nutrientcategory, models.DO_NOTHING,
                                         db_column='NutrientCategory_id')  # Field name made lowercase.

    class Meta:
        app_label = 'admin.nutrientmanage'
        managed = False
        db_table = 'Nutrient'
