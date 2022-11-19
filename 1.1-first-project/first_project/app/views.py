from django.http import HttpResponse
from django.shortcuts import render, reverse
import datetime, os


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('wd')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages,
    }
    return render(request, template_name, context)

def wd_view(request):
    template_name = 'app/wd.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('wd')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    msg = str(os.listdir())
    context = {
        'pages': pages,
        'wd': msg,
    }
    return render(request, template_name, context)

def time_view(request):
    template_name = 'app/time.html'
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('wd')
    }
    current_time = datetime.datetime.now()
    msg = f'Текущее время: {current_time}'
    context = {
        'pages': pages,
        'time': msg,
    }
    return render(request, template_name, context)


