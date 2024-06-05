from django.contrib import admin
from django.urls import path
from moekopienie import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('shop/', views.shop, name='shop'),
    path('product/', views.product, name='product'),
]

