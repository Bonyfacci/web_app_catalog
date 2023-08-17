from django.shortcuts import render

from catalog.models import Product, Category


def home(request):
    data = {
        'categories': Category.objects.all(),
        'title': 'Каталог товаров'
    }
    return render(request, 'main/home.html', data)


def products(request, pk):
    category_name = Category.objects.get(pk=pk)
    data = {
        'products': Product.objects.filter(category=pk),
        'title': f'Каталог товаров - {category_name.name}'
    }
    return render(request, 'main/products.html', data)


def article(request, pk):
    product = Product.objects.get(pk=pk)
    data = {
        'products': product,
        'title': f'{product.name}'
    }
    return render(request, 'main/article.html', data)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Имя: {name}\nТелефон: {phone}\nСообщение: {message}')

    return render(request, 'main/contacts.html')
