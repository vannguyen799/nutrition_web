import hashlib

from django.db import models

# Create your models here.


class Permission(models.Model):
    name = models.CharField(unique=True, max_length=100)

    class Meta:
        app_label = 'admin_auth'
        managed = False
        db_table = 'permission'


class User(models.Model):
    username = models.CharField(unique=True, max_length=50)
    password = models.CharField(max_length=100)
    email = models.CharField(unique=True, max_length=100)
    phone_number = models.IntegerField(unique=True, blank=True, null=True)
    created_date = models.DateTimeField()
    is_locked = models.BinaryField(default=0)  # This field type is a guess.
    is_active = models.BinaryField(blank=True, null=True)  # This field type is a guess.
    permission = models.ForeignKey(Permission, models.DO_NOTHING)

    class Meta:
        app_label = 'admin_auth'
        managed = False
        db_table = 'user'

    @staticmethod
    def hash_password(password):
        password_bytes = password.encode('utf-8')
        sha256_hash = hashlib.sha256()
        sha256_hash.update(password_bytes)
        hashed_password = sha256_hash.hexdigest()
        return hashed_password
