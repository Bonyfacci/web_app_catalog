from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import HomeListView, contacts, ProductListView, ProductCreateView, ProductUpdateView, \
    ArticleDetailView, ProductDeleteView, NewsListView, NewsCreateView, NewsUpdateView, NewsDeleteView, \
    NewsArticleDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('contacts/', contacts, name='contacts'),

    path('products/<int:pk>/', ProductListView.as_view(), name='products'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/edit/<int:pk>/', ProductUpdateView.as_view(), name='product_edit'),
    path('products/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('article/<int:pk>/', cache_page(60)(ArticleDetailView.as_view()), name='article'),

    path('news/', NewsListView.as_view(), name='news'),
    path('news/create/', NewsCreateView.as_view(), name='news_create'),
    path('news/edit/<int:pk>/', NewsUpdateView.as_view(), name='news_edit'),
    path('news/delete/<int:pk>/', NewsDeleteView.as_view(), name='news_delete'),
    path('news/article/<int:pk>/', NewsArticleDetailView.as_view(), name='news_article'),
]
