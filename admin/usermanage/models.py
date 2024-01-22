from django.db import models

# Create your models here.
from admin.admin_auth.models import User, Permission


class Userdetail(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    address = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(User, models.DO_NOTHING)

    class Meta:
        app_label = 'usermanage'
        managed = False
        db_table = 'UserDetail'
