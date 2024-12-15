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
    context = {
        'title': title,
        'text': text,
    }
    return render(request, 'games.html', context)


def cart(request):
    title = 'cart'
    text = 'Извините, в данный момент покупка игр недоступна в вашем регионе'
    context = {
        'title': title,
        'text': text,
    }
    return render(request, 'cart.html', context)
