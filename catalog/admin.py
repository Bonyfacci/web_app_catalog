from django.contrib import admin

from catalog.models import Product, Category, News


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'price', 'category', )
    list_filter = ('category', )
    search_fields = ('name', 'description', )


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'photo', 'created_at', 'is_active', 'views_count')
