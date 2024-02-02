from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import Http404
from django.shortcuts import render

from bs4 import BeautifulSoup
from .models import *
from user.config import item_per_page


# Create your views here.

def index(request):
    # print(request.GET)
    items = None
    search = request.GET.get('search')
    category = request.GET.get('category')
    if None not in [search, category]:
        page = request.GET.get('page')

        articles_ = FoodArticle.objects.filter(title__contains=search).order_by('last_update_date')

        articles = []
        if category not in [None, '']:
            for article in articles_:
                for foodfoodcategory in article.food.categories:
                    if foodfoodcategory.foodcategory.id == int(category):
                        articles.append(article)
        else:
            articles = articles_


        paginator = Paginator(articles, item_per_page)
        try:
            items = paginator.page(page)
        except PageNotAnInteger:
            items = paginator.page(1)
        except EmptyPage:
            items = paginator.page(paginator.num_pages)


    return render(request, 'user/foodarticle/foodarticle.html', context={
        'categories': Foodcategory.objects.all(),
        'items': items
    })


def article_view(request, slug_id):
    try:
        foodarticle = FoodArticle.objects.get(slug_id=slug_id)
    except FoodArticle.DoesNotExist:
        raise Http404("Not Found Article with slug {}".format(slug_id))
    # for foodarticle in FoodArticle.objects.all():
    #     # print(foodarticle.content)
    #     html = BeautifulSoup(foodarticle.content, 'html.parser', from_encoding='utf-8')

    # imgs = html.find_all('img')
    # for img in imgs:
    #     # print(img)
    #     # img.set_attr('style', 'align: center;')
    #     if img.has_attr('data-lazy-src') and not img['src'].startswith('http'):
    #         img['src'] = img['data-lazy-src']

    # noscripts = html.find_all('noscript')
    #
    # if noscripts:
    #     for noscript in noscripts:
    #         noscript.extract()
    # foodarticle.content = html.prettify()
    # foodarticle.save()

    return render(request, 'user/foodarticle/article_view.html', context={'foodarticle': foodarticle})
