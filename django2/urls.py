from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from django2 import settings
from products.views import index_page, ShopPageView, AboutPageView, login, RegisterUser


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page, name='home'),
    path('shop/', ShopPageView.as_view(), name='shop'),
    path('login/', login, name='login'),
    path('register/', RegisterUser.as_view(), name='register')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
