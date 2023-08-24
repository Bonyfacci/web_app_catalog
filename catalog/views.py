from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from pytils.translit import slugify

from catalog.models import Product, Category, News


class HomeListView(ListView):
    model = Category
    template_name = 'main/home.html'
    extra_context = {
        'title': f'Каталог товаров'
    }


class ProductListView(ListView):
    model = Product
    template_name = 'main/product_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category_id=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        category_name = Category.objects.get(pk=self.kwargs.get('pk'))
        context_data['category_pk'] = category_name.pk
        context_data['title'] = f'Каталог товаров - {category_name.name}'

        return context_data


class ProductCreateView(CreateView):
    model = Product
    template_name = 'main/product_form.html'
    fields = ('name', 'category', 'price', 'description')
    success_url = reverse_lazy('catalog:home')


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'main/product_form.html'
    fields = ('name', 'category', 'price', 'photo', 'description')

    def get_success_url(self):
        return reverse('catalog:products', args=[self.object.category_id])


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'main/product_detele_confirm.html'
    success_url = reverse_lazy('catalog:home')


class ArticleDetailView (DetailView):
    model = Product
    template_name = 'main/article.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(pk=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        product_name = Product.objects.get(pk=self.kwargs.get('pk'))
        context_data['title'] = f'Каталог товаров - {product_name.name}'

        return context_data


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Имя: {name}\nТелефон: {phone}\nСообщение: {message}')

    return render(request, 'main/contacts.html')


# ==============================Blog==============================


class NewsListView(ListView):
    model = News
    template_name = 'news/blog.html'
    extra_context = {
        'title': f'Новости Castellsefels'
    }

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_active=True)
        return queryset


class NewsCreateView(CreateView):
    model = News
    template_name = 'news/blog_form.html'
    fields = ('title', 'slug', 'content', 'photo', 'created_at', 'is_active')
    success_url = reverse_lazy('catalog:news')

    def form_valid(self, form):
        if form.is_valid():
            new_news = form.save()
            new_news.slug = slugify(new_news.title)
            new_news.save()

        return super().form_valid(form)


class NewsUpdateView(UpdateView):
    model = News
    template_name = 'news/blog_form.html'
    fields = ('title', 'slug', 'content', 'photo', 'created_at', 'is_active')

    def get_success_url(self):
        return reverse('catalog:news_article', args=[self.object.pk])

    def form_valid(self, form):
        if form.is_valid():
            new_news = form.save()
            new_news.slug = slugify(new_news.title)
            new_news.save()

        return super().form_valid(form)


class NewsDeleteView(DeleteView):
    model = News
    template_name = 'news/blog_delete_confirm.html'
    success_url = reverse_lazy('catalog:news')


class NewsArticleDetailView(DetailView):
    model = News
    template_name = 'news/news_article.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(pk=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        news_title = News.objects.get(pk=self.kwargs.get('pk'))
        context_data['title'] = f'Новости - {news_title.title}'

        return context_data

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object
