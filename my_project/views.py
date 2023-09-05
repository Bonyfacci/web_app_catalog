# import requests
from django.shortcuts import render
from .models import Articles


def my_project(request):
    return render(request, 'my_project/my_project.html')


def about(request):
    # news = Articles.objects.all()
    # news = Articles.objects.order_by('-date')
    # return render(request, 'my_project/about.html', {'news': news})
    return render(request, 'my_project/about.html')


def news(request):
    return render(request, 'my_project/news.html')


def info(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Имя: {name}\nТелефон: {phone}\nСообщение: {message}')

    return render(request, 'my_project/info.html')


def test(request):
    return render(request, 'my_project/test.html')


def exchange(request):
    response = requests.get(url='https://api.exchangerate-api.com/v4/latest/USD').json()
    currencies = response.get('rates')

    if request.method == 'GET':
        context = {
            'currencies': currencies
        }

        return render(request=request, template_name='exchange_app/index.html', context=context)

    if request.method == 'POST':
        from_amount = float(request.POST.get('from-amount'))
        from_curr = request.POST.get('from-curr')
        to_curr = request.POST.get('to-curr')

        converted_amount = round((currencies[to_curr] / currencies[from_curr]) * float(from_amount), 2)

        context = {
            'from_curr': from_curr,
            'to_curr': to_curr,
            'from_amount': from_amount,
            'currencies': currencies,
            'converted_amount': converted_amount
        }

        return render(request=request, template_name='exchange_app/index.html', context=context)
