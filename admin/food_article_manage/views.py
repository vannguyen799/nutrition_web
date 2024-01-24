from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from .models import *
from admin.config import item_per_page
from decorator import require


# Create your views here.

@require.admin
def index(request):
    items = None
    page = request.GET.get('page')

    articles = FoodArticle.objects.all()
    paginator = Paginator(articles, item_per_page)

    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)
    return render(request, 'admin/foodmanage/food_article_index.html', {'articles': items})


@require.admin
def edit_article(request):
    article_id = request.GET.get('id')
    article = FoodArticle.objects.get(pk=article_id)

    return render(request, 'admin/food_article/edit_food_article.html', context={'article': article})