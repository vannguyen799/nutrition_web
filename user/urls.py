
from django.urls import path, include
from .home import urls as home_urls
from .user_auth import urls as user_auth_urls
from .foodarticle import urls as foodarticle_urls

urlpatterns = [
        path('', include(home_urls)),
        path('auth/', include(user_auth_urls)),
        path('cong_thuc/', include(foodarticle_urls))
]