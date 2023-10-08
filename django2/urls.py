from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from django2 import settings
from products.views import index_page, ShopPageView, AboutPageView, send_form

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page, name='home'),
    path('shop', ShopPageView.as_view(), name='shop'),
    path('abouts', AboutPageView.as_view(), name='about'),
    path('form', send_form),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
