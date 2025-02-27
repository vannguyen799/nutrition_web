# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Dish(models.Model):
    name = models.CharField(unique=True, max_length=100)
    image = models.CharField(max_length=200)
    kcal = models.IntegerField()
    refuse_rate = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    dishcategory = models.ForeignKey('Dishcategory', models.DO_NOTHING, db_column='DishCategory_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dish'


class DishNutrient(models.Model):
    dish = models.OneToOneField(Dish, models.DO_NOTHING, db_column='Dish_id', primary_key=True)  # Field name made lowercase. The composite primary key (Dish_id, Nutrient_id) found, that is not supported. The first column is selected.
    nutrient = models.ForeignKey('Nutrient', models.DO_NOTHING, db_column='Nutrient_id')  # Field name made lowercase.
    value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dish_nutrient'
        unique_together = (('dish', 'nutrient'),)


class Dishcategory(models.Model):
    name = models.CharField(unique=True, max_length=100)
    description = models.TextField(blank=True, null=True)
    dishcategory = models.ForeignKey('self', models.DO_NOTHING, db_column='DishCategory_id', blank=True, null=True)  # Field name made lowercase.
    image = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dishcategory'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Food(models.Model):
    name = models.CharField(unique=True, max_length=100)
    description = models.TextField(blank=True, null=True)
    image = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'food'


class FoodDish(models.Model):
    food = models.OneToOneField(Food, models.DO_NOTHING, db_column='Food_id', primary_key=True)  # Field name made lowercase. The composite primary key (Food_id, Dish_id) found, that is not supported. The first column is selected.
    dish = models.ForeignKey(Dish, models.DO_NOTHING, db_column='Dish_id')  # Field name made lowercase.
    value = models.FloatField()
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'food_dish'
        unique_together = (('food', 'dish'),)


class FoodFoodcategory(models.Model):
    food = models.OneToOneField(Food, models.DO_NOTHING, db_column='Food_id', primary_key=True)  # Field name made lowercase. The composite primary key (Food_id, FoodCategory_id) found, that is not supported. The first column is selected.
    foodcategory = models.ForeignKey('Foodcategory', models.DO_NOTHING, db_column='FoodCategory_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'food_foodcategory'
        unique_together = (('food', 'foodcategory'),)


class Foodarticle(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.CharField(max_length=200, blank=True, null=True)
    time_spend = models.IntegerField()
    created_date = models.DateTimeField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_published = models.IntegerField(blank=True, null=True)
    food = models.ForeignKey(Food, models.DO_NOTHING, db_column='Food_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'foodarticle'


class Foodarticlecomment(models.Model):
    foodarticle = models.ForeignKey(Foodarticle, models.DO_NOTHING, db_column='FoodArticle_id')  # Field name made lowercase.
    content = models.TextField()
    rate = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    is_hidden = models.IntegerField(blank=True, null=True)
    is_anonymous = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING, db_column='User_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'foodarticlecomment'


class Foodcategory(models.Model):
    name = models.CharField(unique=True, max_length=100)
    description = models.TextField(blank=True, null=True)
    image = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'foodcategory'


class Foodmenu(models.Model):
    foodmenulist = models.ForeignKey('Foodmenulist', models.DO_NOTHING, db_column='FoodMenuList_id')  # Field name made lowercase.
    for_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'foodmenu'


class FoodmenuFood(models.Model):
    foodmenu = models.OneToOneField(Foodmenu, models.DO_NOTHING, db_column='FoodMenu_id', primary_key=True)  # Field name made lowercase. The composite primary key (FoodMenu_id, Food_id) found, that is not supported. The first column is selected.
    food = models.ForeignKey(Food, models.DO_NOTHING, db_column='Food_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'foodmenu_food'
        unique_together = (('foodmenu', 'food'),)


class Foodmenulist(models.Model):
    name = models.CharField(max_length=100)
    created_date = models.DateField()
    peoplegroup = models.ForeignKey('Peoplegroup', models.DO_NOTHING, db_column='PeopleGroup_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'foodmenulist'


class Nutrient(models.Model):
    name = models.CharField(unique=True, max_length=100)
    unit = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    nutrientcategory = models.ForeignKey('Nutrientcategory', models.DO_NOTHING, db_column='NutrientCategory_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nutrient'


class Nutrientcategory(models.Model):
    name = models.CharField(unique=True, max_length=100)
    description = models.TextField(blank=True, null=True)
    image = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nutrientcategory'


class People(models.Model):
    name = models.CharField(max_length=100)
    height = models.FloatField()
    weight = models.FloatField()
    age = models.IntegerField()
    gender = models.IntegerField()
    relationship = models.CharField(max_length=100, blank=True, null=True)
    peoplegroup = models.ForeignKey('Peoplegroup', models.DO_NOTHING, db_column='PeopleGroup_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'people'


class Peoplegroup(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey('User', models.DO_NOTHING, db_column='User_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'peoplegroup'


class Permission(models.Model):
    name = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'permission'


class User(models.Model):
    username = models.CharField(unique=True, max_length=50)
    password = models.CharField(max_length=100)
    email = models.CharField(unique=True, max_length=100)
    phone_number = models.IntegerField(unique=True, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    is_locked = models.IntegerField()
    is_active = models.IntegerField()
    permission = models.ForeignKey(Permission, models.DO_NOTHING)
    firstname = models.CharField(max_length=100, blank=True, null=True)
    lastname = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
