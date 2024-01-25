from django.shortcuts import render

from admin.food_article_manage.models import FoodArticle


# Create your views here.
def index(request):
    banner_food_articles = FoodArticle.objects.order_by('created_date')[:4]

    # FoodArticle.create_slug_id(FoodArticle.objects)
    return render(request, 'user/index.html', context={
        'banner_food_articles': {
            'one': banner_food_articles[0],
            'two': banner_food_articles[1],
            'three': banner_food_articles[2],
            'four': banner_food_articles[3],
        }
    })
