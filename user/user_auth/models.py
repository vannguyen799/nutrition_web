from django.db import models

# Create your models here.

from admin.admin_auth.models import User, Permission

# class User(User):
#
#     class Meta:
#         app_label = 'user_auth'
#         managed = False
#         db_table = 'User'


# class Permission(Permission):
#     class Meta:
#         app_label = 'user_auth'
#         db_table = Permission._meta.db_table