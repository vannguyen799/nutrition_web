from sqlite3 import IntegrityError
from django.shortcuts import render, redirect
from django.utils import timezone

from decorator import require
from admin.dishmanage.models import Dish
from admin.foodmanage.models import Food, Foodcategory, FoodFoodcategory, FoodDish, Foodarticle


# Create your views here.
@require.admin
def index(request):
    if request.method == 'GET':
        return render(request, 'admin/foodmanage/food_manage.html', {'foods': Food.objects.all()})


@require.admin
@require.post_form('name', 'categories')
def add_food(request):
    context = {
        'food_category': Foodcategory.objects.all(),
        'dish': Dish.objects.all()
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        categories_id = request.POST.get('categories')

        dishes_id = request.POST.get('dishes')
        dish_count = request.POST.get('dish_count')
        dish_value = request.POST.get('dish_value')

        food_article = request.POST.get('food_article')
        is_publish = request.POST.get('is_publish')
        time_spend = request.POST.get('time_spend')
        try:
            # add food
            food = Food.objects.create(name=name, description=description, image=image)
            # add category for food
            for category in categories_id.split(','):
                FoodFoodcategory.objects.create(food.id, category)
            # add dish infor for food
            if dishes_id is not None:
                for i in range(len(dishes_id)):
                    FoodDish.objects.create(food_id=food.id, dish_id=dishes_id[i], value=dish_value[i],
                                            count=dish_count[i])
            # add food article
            Foodarticle.objects.create(
                food_id=food.id,
                content=food_article,
                time_spend=time_spend,
                created_date=timezone.now(),
                last_update_date=timezone.now(),
                is_published=1 if is_publish == 'on' else 0,
                image=image
            )
        except IntegrityError:
            context['message'] = 'Food already exists'
        except Exception as e:
            context['message'] = str(e)

    return render(request, 'admin/foodmanage/add_food.html', context=context)


@require.admin
def delete_food(request):
    if request.method == 'POST':
        food_id = request.POST.get('id')
        Food.objects.filter(id=food_id).delete()
    return redirect('admin_foodmanage')


@require.admin
def update_food(request):
    food_id = request.POST.get('id')
    pass


@require.admin
def manage_food_categories(request):
    return render(request, 'admin/foodmanage/food_category_manage.html', context={
        'food_category': Foodcategory.objects.all()
    })


@require.admin
def add_food_category(request):
    context = {'dish': Dish.objects.all()}
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        image_file = request.FILES.get('image')
        if image_file:
            image_file.name = f'{timezone.now()}.{image_file.name}'
        try:
            Foodcategory.objects.create(name=name, description=description, image=image_file)
            context['message'] = 'add food category successfully'
        except IntegrityError:
            context['message'] = 'duplicate food category'
            context['name'] = name
            context['description'] = description

    return render(request, 'admin/foodmanage/add_food_category.html', context=context)


@require.admin
def delete_food_category(request, food_category_id):
    if request.method == 'POST':
        Foodcategory.objects.filter(id=food_category_id).delete()
    return redirect('admin_foodcategory')


@require.admin
def edit_food_category(request):
    if request.method == 'POST':
        image_file = request.FILES.get('image')
        if image_file:
            image_file.name = f'{timezone.now()}.{image_file.name}'
        food_category_id = request.POST.get('id')
        print(food_category_id)
        food_category = Foodcategory.objects.get(id=food_category_id)
        food_category.name = request.POST.get('name')
        food_category.description = request.POST.get('description')
        food_category.image = image_file
        food_category.save()
        return redirect('admin_foodcategory')

    if request.method == 'GET':
        food_category_id = request.GET.get('id')
        return render(request, 'admin/foodmanage/edit_food_category.html', context={
            'food_category': Foodcategory.objects.get(pk=food_category_id)
        })
