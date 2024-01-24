from django.apps import AppConfig
from admin import admin_auth


class AuthConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = "admin.admin_auth"
