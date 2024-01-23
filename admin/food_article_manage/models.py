from django.db import models

from admin.foodmanage.models import Food


# Create your models here.
class Foodarticle(models.Model):
    content = models.TextField()
    food = models.ForeignKey(Food, models.DO_NOTHING, db_column='Food_id')  # Field name made lowercase.
    time_spend = models.IntegerField()
    title = models.TextField(default='no title', max_length=200)
    created_date = models.DateTimeField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_published = models.BinaryField(blank=True, null=True)  # This field type is a guess.
    image = models.ImageField(upload_to='admin/img/', blank=True, null=True)

    class Meta:
        app_label = 'admin.foodmanage'
        managed = False
        db_table = 'FoodArticle'
