from django.db import models
from django.utils.text import slugify

from admin.foodmanage.models import Food



# Create your models here.
class FoodArticle(models.Model):
    content = models.TextField()
    time_spend = models.IntegerField()
    slug_id = models.SlugField(unique=True, null=True, blank=True, db_column='slug_id')
    title = models.TextField(default='no title', max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    last_update_date = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    image = models.ImageField(upload_to='admin/img/', blank=True, null=True)

    food = models.ForeignKey(Food, models.DO_NOTHING, db_column='Food_id')  # Field name made lowercase.

    class Meta:
        app_label = 'admin.food_article_manage'
        managed = False
        db_table = 'FoodArticle'

    def save(self, *args, **kwargs):
        if not self.slug_id:
            self.slug_id = slugify('{}-{}'.format(self.title, self.created_date))
        super(FoodArticle, self).save(*args, **kwargs)

    @property
    def get_slug(self):
        if not self.slug_id:
            self.slug_id = slugify('{}-{}'.format(self.title, self.created_date))
        return self.slug_id

    @staticmethod
    def create_slug_id(model_objects):
        for obj in model_objects.all():
            obj.save()
            print(obj.slug_id)


class FoodArticleComment(models.Model):
    foodarticle = models.ForeignKey(FoodArticle, models.DO_NOTHING, db_column='FoodArticle_id')  # Field name made lowercase.
    content = models.TextField()
    rate = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    is_hidden = models.BooleanField(default=False)
    is_anonymous = models.BooleanField(default=False)

    user = models.ForeignKey('admin_auth.User', models.DO_NOTHING, db_column='User_id')  # Field name made lowercase.

    class Meta:
        app_label = 'admin.food_article_manage'
        managed = False
        db_table = 'foodarticlecomment'