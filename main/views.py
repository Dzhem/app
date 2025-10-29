from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {
        "title": "Home - Главная",
        "content": "Магазин мебели HOME",
    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        "title": "Home - О нас",
        "title_on_page": "О нас",
        "content": "Текст о том какой классный этот интернет магазин.",
    }
    return render(request, 'main/about.html', context)
