import hashlib

from django.db import models

# Create your models here.


class Permission(models.Model):
    name = models.CharField(unique=True, max_length=100)

    class Meta:
        app_label = 'admin_auth'
        managed = False
        db_table = 'Permission'


class User(models.Model):
    username = models.CharField(unique=True, max_length=50)
    password = models.CharField(max_length=100)
    email = models.CharField(unique=True, max_length=100)
    phone_number = models.IntegerField(unique=True, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    is_locked = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    permission = models.ForeignKey(Permission, models.DO_NOTHING)
    firstname = models.CharField(max_length=100, default='unknown')
    lastname = models.CharField(max_length=100, default='unknown')
    address = models.CharField(max_length=100, default='unknown')


    class Meta:
        app_label = 'admin_auth'
        managed = False
        db_table = 'User'

    @staticmethod
    def hash_password(password):
        password_bytes = password.encode('utf-8')
        sha256_hash = hashlib.sha256()
        sha256_hash.update(password_bytes)
        hashed_password = sha256_hash.hexdigest()
        return hashed_password
