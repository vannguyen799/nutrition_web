
from admin.admin_auth import urls as admin_auth_urls
from .usermanage import urls as user_manage_urls
from .dashboard import urls as dashboard_urls
from .foodmanage import urls as foodmanage_urls
from .food_article_manage import urls as food_article_manage_urls
from django.urls import path, include

urlpatterns = [
        path('', include(dashboard_urls)),
        path('dashboard/', include(dashboard_urls)),
        path('auth/', include(admin_auth_urls)),
        path('usermanage/', include(user_manage_urls)),
        path('foodmanage/', include(foodmanage_urls)),
        path('food_article/', include(food_article_manage_urls))
]
