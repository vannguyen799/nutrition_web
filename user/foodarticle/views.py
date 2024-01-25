from django.shortcuts import render

from admin.food_article_manage.models import FoodArticle


# from .models import FoodArticle


# Create your views here.

def index(request):
    pass


def article_view(request, slug_id):
    foodarticle = FoodArticle.objects.get(slug_id=slug_id)

    return render(request, 'user/foodarticle/article_view.html', context={'foodarticle': foodarticle})
