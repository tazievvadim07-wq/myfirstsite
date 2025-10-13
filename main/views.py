from django.shortcuts import render

def home_view(request):
    return render(request, 'main/home.html')

def news_view(request):
    news = [
        {"title": "Django 5.0 вышел!", "text": "Вышла новая версия Django."},
        {"title": "Python 3.13", "text": "Добавлены новые возможности!"},
    ]
    return render(request, 'news.html', {'news': news})
