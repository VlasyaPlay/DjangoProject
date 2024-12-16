from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def platform(request):
    title = 'platform'
    text = 'Главная страница'
    context = {
        'title': title,
        'text': text,
    }
    return render(request, 'platform.html', context)


def shop(request):
    title = 'games'
    text = 'Игры'
    games = [
        'Hunt Showdown 1896',
        'Mass Effect Legendary Edition',
        'Ведьмак 3: Дикая охота',
    ]
    context = {
        'title': title,
        'text': text,
        'games': games,
    }
    return render(request, 'games.html', context)


def cart(request):
    title = 'cart'
    text = 'Корзина'
    content = 'Извините, покупка игр временно недоступна'
    context = {
        'title': title,
        'content': content,
        'text': text,
    }
    return render(request, 'cart.html', context)
