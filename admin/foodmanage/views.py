from sqlite3 import IntegrityError

from django.shortcuts import render, redirect
from django.utils import timezone
from admin.foodmanage.models import Food, Foodcategory
from decorator import require_admin


# Create your views here.
@require_admin
def index(request):
    if request.method == 'GET':
        return render(request, 'admin/foodmanage/food_manage.html', {'foods': Food.objects.all()})


@require_admin
def add_food(request):
    if request.method == 'POST':
        pass
    print(Foodcategory.objects.all().__str__())
    return render(request, 'admin/foodmanage/add_food.html', context={
        'food_category': Foodcategory.objects.all()
    })


@require_admin
def delete_food(request, food_id):
    pass


@require_admin
def update_food(request, food_id):
    pass


@require_admin
def manage_food_categories(request):
    return render(request, 'admin/foodmanage/food_category_manage.html', context={
        'food_category': Foodcategory.objects.all()
    })


@require_admin
def add_food_category(request):
    context = {}
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


@require_admin
def delete_food_category(request, food_category_id):
    if request.method == 'POST':
        Foodcategory.objects.filter(id=food_category_id).delete()
    return redirect('admin_foodcategory')


@require_admin
def edit_food_category(request):
    food_category_id = request.GET.get('id')
    if request.method == 'POST':
        try:
            image_file = request.FILES.get('image')
            if image_file:
                image_file.name = f'{timezone.now()}.{image_file.name}'

            food_category = Foodcategory.objects.get(pk=food_category_id)
            food_category.name = request.POST.get('name')
            food_category.description = request.POST.get('description')
            food_category.image = image_file
            food_category.save()

            print(f'updated food category successfully {food_category_id}')
            return redirect('admin_foodcategory')
        except Foodcategory.DoesNotExist:
            pass
    return render(request, 'admin/foodmanage/edit_food_category.html', context={
        'food_category': Foodcategory.objects.get(pk=food_category_id)
    })
