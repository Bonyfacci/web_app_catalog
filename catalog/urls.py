from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import home, contacts, products, article

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('<int:pk>/products/', products, name='products'),
    path('<int:pk>/article/', article, name='article'),
]
