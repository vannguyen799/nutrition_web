from django.db import models

from admin.admin_auth.models import User


# Create your models here.

class Peoplegroup(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, models.DO_NOTHING, db_column='User_id')  # Field name made lowercase.

    class Meta:
        app_label = 'admin.foodmanage'

        managed = False
        db_table = 'PeopleGroup'

class People(models.Model):
    name = models.CharField(max_length=100)
    height = models.FloatField()
    weight = models.FloatField()
    age = models.IntegerField()
    gender = models.TextField()  # This field type is a guess.
    relationship = models.CharField(max_length=100, blank=True, null=True)
    peoplegroup = models.ForeignKey(Peoplegroup, models.DO_NOTHING,
                                    db_column='PeopleGroup_id')  # Field name made lowercase.

    class Meta:
        app_label = 'admin.foodmanage'

        managed = False
        db_table = 'People'



