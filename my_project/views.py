from django.shortcuts import render
from .models import Articles


def my_project(request):
    return render(request, 'my_project/my_project.html')


def about(request):
    news = Articles.objects.all()
    # news = Articles.objects.order_by('-date')
    return render(request, 'my_project/about.html', {'news': news})


def news(request):
    return render(request, 'my_project/news.html')


def info(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Имя: {name}\nТелефон: {phone}\nСообщение: {message}')

    return render(request, 'my_project/info.html')
