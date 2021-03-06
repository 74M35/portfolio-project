from django.contrib import admin
from django.urls import path, include
from products import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='PHhome'),
    path('accounts/', include('accounts.urls')),
    path('products/', include('products.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
